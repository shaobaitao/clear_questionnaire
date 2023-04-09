# Create your views here.
import datetime

from django.db.models import Q, Avg
from django.core.paginator import Paginator

from django_clear_questionnaire import settings
from user.decorators.user import jsonLoad
from questionnaire.decorators.index import *
from questionnaire.models import *
from tools.index import *
from user.decorators.user import tokenCheck
from user.models import USER_INFO

from ua_parser import user_agent_parser
import base64
from django.core.files.base import ContentFile


def index(request):
    return HttpResponse('ok')


@jsonLoad
@tokenCheck
@createCheck
def create(request):
    userID = request.payload['id']
    title = request.POST['title']
    desc = request.POST['desc']
    project = PROJECT.objects.create(
        title=title,
        desc=desc,
        state=0,
        user_id=userID
    )
    data = {'projectID': project.id}
    return codeMsg(20200, "问卷创建成功", data)


@jsonLoad
@tokenCheck
def getProjects(request):
    id = request.payload['id']
    page = request.POST['projectPage']
    perPage = 10

    paginator = Paginator(PROJECT.objects.filter(Q(user=id) & ~Q(state=2)).order_by('-created_time'), perPage)
    projects = paginator.get_page(page)
    jsonList = querySetToList(projects)
    for inx, dic in enumerate(jsonList):
        dic['created_time'] = int(time.mktime(projects[inx].created_time.timetuple()))

    return codeMsg(20201, "项目列表获取成功", jsonList)


@tokenCheck
def getProjectsCount(request):
    id = request.payload['id']
    count = PROJECT.objects.filter(Q(user=id) & ~Q(state=2)).count()
    return codeMsg(20202, "项目数量获取成功", count)


@jsonLoad
@tokenCheck
@questionPermissionCheck
def publishProject(request):
    id = request.POST['projectID']

    # 1 是已发布
    if not QUESTION.objects.filter(project_id=id).count():
        return codeMsg(20301, "问卷至少要有一个题目才能发布")

    project = PROJECT.objects.get(id=id)
    project.state = 1
    project.save()
    return codeMsg(20209, "发布项目成功")


@jsonLoad
@tokenCheck
@questionPermissionCheck
def suspendProject(request):
    id = request.POST['projectID']

    project = PROJECT.objects.get(id=id)
    project.state = 0
    # 2 是暂停 未发布
    project.save()
    return codeMsg(20210, "暂停项目成功")


@jsonLoad
@tokenCheck
@questionPermissionCheck
def deleteProject(request):
    id = request.POST['projectID']

    project = PROJECT.objects.get(id=id)
    project.state = 2
    # 2 是已删除
    project.save()
    return codeMsg(20203, "删除项目成功")


@jsonLoad
@tokenCheck
@questionPermissionCheck
@radioCheck
@questionSerialNumber
def createSingleChoice(request):
    question = QUESTION.objects.create(
        title=request.POST['question']['title'],
        required=request.POST['question']['required'],
        type=1,
        desc=request.POST['question']['desc'],
        random=request.POST['question']['random'],
        project_id=request.POST['projectID'],
        serial_number=request.serialNumber
    )
    for optionIndex, option in enumerate(request.POST['question']['options']):
        Q_CHOICE.objects.create(
            question_id=question.id,
            title=option['title'],
            index=optionIndex + 1
        )
    return codeMsg(20204, "单选题创建成功")


@jsonLoad
@tokenCheck
@questionPermissionCheck
@radioCheck
@questionSerialNumber
def createMultipleChoice(request):
    question = QUESTION.objects.create(
        title=request.POST['question']['title'],
        required=request.POST['question']['required'],
        type=2,
        desc=request.POST['question']['desc'],
        random=request.POST['question']['random'],
        project_id=request.POST['projectID'],
        serial_number=request.serialNumber
    )
    for optionIndex, option in enumerate(request.POST['question']['options']):
        Q_CHOICE.objects.create(
            question_id=question.id,
            title=option['title'],
            index=optionIndex + 1
        )
    return codeMsg(20205, "多选题创建成功")


@jsonLoad
@tokenCheck
@questionPermissionCheck
@completionCheck
@questionSerialNumber
def createCompletion(request):
    question = QUESTION.objects.create(
        title=request.POST['question']['title'],
        required=request.POST['question']['required'],
        type=3,
        desc=request.POST['question']['desc'],
        project_id=request.POST['projectID'],
        serial_number=request.serialNumber
    )

    Q_COMPLETION.objects.create(
        question_id=question.id,
        regex=request.POST['question']['regex']
    )
    return codeMsg(20206, "填空题创建成功")


@jsonLoad
@tokenCheck
@questionPermissionCheck
@completionCheck
@questionSerialNumber
def createImage(request):
    question = QUESTION.objects.create(
        title=request.POST['question']['title'],
        required=request.POST['question']['required'],
        type=7,
        desc=request.POST['question']['desc'],
        project_id=request.POST['projectID'],
        serial_number=request.serialNumber
    )

    Q_IMAGE.objects.create(
        question_id=question.id,
        size=request.POST['question']['size'],
        count=request.POST['question']['count'],
    )
    return codeMsg(20206, "图片题创建成功")


def getQuestions(request):
    data = {}
    projectID = request.POST['projectID']

    project = PROJECT.objects.get(id=projectID)
    data['id'] = project.id
    data['creator'] = project.user.username
    data['avatar'] = str(USER_INFO.objects.get(user=project.user).avatar)
    data['title'] = project.title
    data['desc'] = project.desc

    questions = QUESTION.objects.filter(state=1).filter(project=project.id).order_by('serial_number')
    data['questions'] = querySetToList(questions)

    for item in data['questions']:

        if item.get('type') == 1 or item.get('type') == 2:
            options = Q_CHOICE.objects.filter(question_id=item.get('id'))
            options = querySetToList(options)
            item['options'] = options
            item['answer'] = -1 if item.get('type') == 1 else []

        elif item.get('type') == 3:
            regex = Q_COMPLETION.objects.get(question_id=item.get('id'))
            item['regex'] = regex.regex
            item['answer'] = ''

        elif item.get('type') == 7:
            image = Q_IMAGE.objects.get(question_id=item.get('id'))
            item['count'] = image.count
            item['size'] = image.size
            item['answer'] = []

    return codeMsg(20207, "项目问题获取成功", data)


@jsonLoad
@getQuestionsPublicCheck
def getQuestionsPublic(request):
    return getQuestions(request)


@jsonLoad
@tokenCheck
@questionPermissionCheck
def getQuestionsPrivate(request):
    return getQuestions(request)


@jsonLoad
@tokenCheck
@questionPermissionCheck
def deleteQuestion(request):
    question = QUESTION.objects.get(id=request.POST['questionID'])
    question.state = 0
    QUESTION.objects.filter(serial_number__gt=question.serial_number).update(serial_number=F('serial_number') - 1)
    question.serial_number = 0
    question.save()
    return codeMsg(20208, "项目问题删除成功")


@jsonLoad
@tokenCheck
@questionPermissionCheck
def moveQuestion(request):
    direction = request.POST['direction']
    projectID = request.POST['projectID']
    questionID = request.POST['questionID']

    question = QUESTION.objects.get(id=questionID)
    if direction == 0:  # up
        if question.serial_number == 1:
            return codeMsg(20209, "该项目问题不能上移")
        question.serial_number -= 1

        QUESTION.objects.filter(project=projectID).filter(serial_number=question.serial_number).update(
            serial_number=F('serial_number') + 1)
        question.save()

    else:  # down
        serial_number_max = QUESTION.objects.filter(project=projectID).aggregate(Max('serial_number'))[
            'serial_number__max']
        if question.serial_number == serial_number_max:
            return codeMsg(20209, "该项目问题不能下移")
        question.serial_number += 1

        QUESTION.objects.filter(project=projectID).filter(serial_number=question.serial_number).update(
            serial_number=F('serial_number') - 1)
        question.save()
    return codeMsg(20209, "项目问题移动成功")


@jsonLoad
@tokenCheck
@questionPermissionCheck
def getQuestion(request):
    questionID = request.POST['questionID']
    question = QUESTION.objects.filter(id=questionID)
    data = querySetToList(question)

    for item in data:
        if item.get('type') == 1 or item.get('type') == 2:
            options = Q_CHOICE.objects.filter(question_id=item.get('id'))
            options = querySetToList(options)
            item['options'] = options
        elif item.get('type') == 3:
            regex = Q_COMPLETION.objects.get(question_id=item.get('id'))
            item['regex'] = regex.regex

    return codeMsg(20210, "项目单个问题获取成功", data)


@jsonLoad
@tokenCheck
@questionPermissionCheck
@radioCheck
@questionSerialNumber
def editSingleChoice(request):
    questionID = request.POST['question']['id']
    QUESTION.objects.filter(id=questionID).update(
        title=request.POST['question']['title'],
        required=request.POST['question']['required'],
        desc=request.POST['question']['desc'],
        random=request.POST['question']['random'],
    )

    # 这边选项修改比较麻烦
    for option in request.POST['question']['options']:
        Q_CHOICE.objects.filter(id=option['id']).update(
            title=option['title']
        )

    return codeMsg(20204, "单选题编辑成功")


@jsonLoad
@tokenCheck
@questionPermissionCheck
@radioCheck
@questionSerialNumber
def editMultipleChoice(request):
    return None


@jsonLoad
@tokenCheck
@questionPermissionCheck
@completionCheck
@questionSerialNumber
def editCompletion(request):
    return None


def a_radio(answer: int, id: int):
    A_CHOICE.objects.create(
        answer_id=id,
        option_id=answer
    )


def a_checkBox(answer: list, id: int):
    for i in answer:
        A_CHOICE.objects.create(
            answer_id=id,
            option_id=i
        )


def a_completion(answer: str, id: int, qID: int):
    A_COMPLETION.objects.create(
        answer_id=id,
        completion_id=Q_COMPLETION.objects.get(question_id=qID).id,
        content=answer
    )


def a_image(answer: list, id: int):
    for fileIndex, file in enumerate(answer):
        # file['content'] 大概是 data:image/jpeg;base64,/9j/4AAQSkZJRgABAgAAZABkAAD/7AARRHVja 这样
        imgType, imgStr = file['content'].split(';base64,')
        # imgType='data:image/jpeg '
        # imgType.split('/')[-1]='jpeg'
        # imgSt='/9j/4AAQSkZJRgABAgAAZABkAAD/7AARRHVja'
        data = ContentFile(base64.b64decode(imgStr), name=('pic_%d_%d.%s' % (id, fileIndex, imgType.split('/')[-1])))

        A_IMAGE.objects.create(
            answer_id=id,
            url=data
        )


@jsonLoad
def postQuestionnaire(request):
    submit = SUBMIT.objects.create(
        project_id=request.POST['id'],
        duration=request.POST['duration'],
        ip=request.META['REMOTE_ADDR'],
        os=request.META['HTTP_USER_AGENT'],
    )
    typeFunctions = {
        1: lambda answer, id, *qID: a_radio(answer, id),
        2: lambda answer, id, *qID: a_checkBox(answer, id),
        3: lambda answer, id, *qID: a_completion(answer, id, qID),
        7: lambda answer, id, *qID: a_image(answer, id)
    }
    for q in request.POST['questions']:
        if not q['answer']:
            ANSWER.objects.create(
                submit_id=submit.id,
                question_id=q['id'],
                type=q['type'],
                is_null=True
            )
            continue

        ans = ANSWER.objects.create(
            submit_id=submit.id,
            question_id=q['id'],
            type=q['type']
        )
        typeFunctions[q['type']](q['answer'], ans.id, q['id'])
    project = PROJECT.objects.get(id=request.POST['id'])
    project.submits += 1
    project.save()
    return codeMsg(20210, "问卷提交成功")


@jsonLoad
@tokenCheck
@questionPermissionCheck
def getAnalysis(request):
    data = {}
    projectID = request.POST['projectID']
    project = PROJECT.objects.get(id=projectID)
    data['id'] = project.id
    data['creator'] = project.user.username
    data['avatar'] = str(USER_INFO.objects.get(user=project.user).avatar)
    data['title'] = project.title
    data['desc'] = project.desc
    data['submit'] = SUBMIT.objects.filter(project=projectID, state=1).count()
    data['todaySubmit'] = SUBMIT.objects.filter(
        project=projectID,
        state=1,
        submit_time__year=datetime.datetime.now().year,
        submit_time__month=datetime.datetime.now().month,
        submit_time__day=datetime.datetime.now().day
    ).count()
    data['averageDuration'] = SUBMIT.objects.filter(project=projectID, state=1).aggregate(Avg('duration'))[
        'duration__avg']

    questions = QUESTION.objects.filter(project=project.id, state=1).order_by('serial_number')

    data['questions'] = querySetToList(questions)

    for question in data['questions']:
        question['answer'] = None
        totalSubmit = ANSWER.objects.filter(question_id=question.get('id'), submit__state=1).count()
        question['totalSubmit'] = totalSubmit

        if question.get('type') == 1 or question.get('type') == 2:
            options = Q_CHOICE.objects.filter(question_id=question.get('id'))
            options = querySetToList(options)
            for option in options:
                count = A_CHOICE.objects.filter(option=option['id'], answer__submit__state=1).count()
                option['count'] = count

            question['answers'] = options

        elif question.get('type') == 3:
            answers = []
            for answer in A_COMPLETION.objects.filter(
                    completion_id=Q_COMPLETION.objects.get(question_id=question.get('id')), answer__submit__state=1):
                answers.append(answer.content)
            answerDict = {}
            for key in answers:
                answerDict[key] = answerDict.get(key, 0) + 1
            answers = []
            for key in answerDict:
                answers.append({'title': key, 'count': answerDict[key]})
            answers.sort(key=lambda x: x['count'], reverse=True)
            question['answers'] = answers
            regex = Q_COMPLETION.objects.get(question_id=question.get('id'))
            question['regex'] = regex.regex

        elif question.get('type') == 7:
            urls = []
            answers = ANSWER.objects.filter(question_id=question.get('id'))

            for answer in answers:
                if answer.type == 7:
                    images = A_IMAGE.objects.filter(answer_id=answer.id)
                    for img in images:
                        urls.append(settings.IMAGES_URL + str(img.url))

            question['answers'] = urls

    return codeMsg(20211, "项目分析获取成功", data)


@jsonLoad
@tokenCheck
@questionPermissionCheck
def getSubmits(request):
    projectID = request.POST['projectID']
    pageNumber = request.POST['pageNumber']

    pageItems = 10
    paginator = Paginator(SUBMIT.objects.filter(project=projectID, state=1).order_by('id'),
                          pageItems)  # Show 25 contacts per page.
    data = {}
    submitList = []
    for submitIndex, submit in enumerate(paginator.get_page(pageNumber)):
        jsonDict = submit.to_dict()
        jsonDict['index'] = (pageNumber - 1) * pageItems + submitIndex + 1
        submitList.append(jsonDict)

    data['submitList'] = submitList
    data['pageCount'] = paginator.num_pages
    return codeMsg(20212, "项目问卷提交数据获取成功", data)


@jsonLoad
@tokenCheck
@questionPermissionCheck
def downloadData(request):
    projectID = request.POST['projectID']
    mode = request.POST['mode']

    submits = SUBMIT.objects.filter(
        project=projectID,
        state=1
    )
    data = []
    # 这里是表格的第一行数据，第一行都是问题的标题
    row = ['序号', '提交时间', '用时（毫秒）', '提交IP', '浏览器', '操作系统']

    if mode == 1:
        for qIndex, answer in enumerate(ANSWER.objects.filter(submit_id=submits[0].id)):
            row.append(str(qIndex + 1) + '.' + answer.question.title)
        data.append(row)

        # 这里就是表格各行的数据了
        for submitIndex, submit in enumerate(submits):
            row = [
                str(submitIndex + 1),
                submit.submit_time.strftime('%Y-%m-%d %H:%I:%S'),
                str(submit.duration),
                str(submit.ip),
                # '', #提交地点
                str(user_agent_parser.ParseUserAgent(submit.os)['family']),
                str(user_agent_parser.ParseOS(submit.os)['family'])
            ]

            answers = ANSWER.objects.filter(submit_id=submit.id)
            for answer in answers:
                if answer.is_null:
                    row.append('')

                elif answer.type == 1:
                    choice = A_CHOICE.objects.get(answer_id=answer.id)
                    row.append(choice.option.title)

                elif answer.type == 2:
                    content = ''
                    choices = A_CHOICE.objects.filter(answer_id=answer.id)
                    for choiceIndex, choice in enumerate(choices):
                        content += choice.option.title if choiceIndex == 0 else '┋' + choice.option.title
                    row.append(content)

                elif answer.type == 3:
                    # noinspection PyBroadException
                    try:
                        completion = A_COMPLETION.objects.get(answer_id=answer.id)
                        row.append(completion.content)
                    except:
                        row.append('')

                elif answer.type == 7:
                    urls = ''
                    images = A_IMAGE.objects.filter(answer_id=answer.id)
                    for imgIndex, img in enumerate(images):
                        url = settings.IMAGES_URL + str(img.url)
                        urls += url if imgIndex == 0 else '┋' + url
                    row.append(urls)

            data.append(row)
    elif mode == 2:
        for qIndex, answer in enumerate(ANSWER.objects.filter(submit_id=submits[0].id)):
            if answer.type == 2:
                choices = Q_CHOICE.objects.filter(question_id=answer.question.id)
                for choice in choices:
                    row.append(str(qIndex + 1) + '.(' + choice.title + ')')
                continue
            row.append(str(qIndex + 1) + '.' + answer.question.title)
        data.append(row)

        for submitIndex, submit in enumerate(submits):
            row = [
                str(submitIndex + 1),
                submit.submit_time.strftime('%Y-%m-%d %H:%I:%S'),
                str(submit.duration),
                str(submit.ip),
                # '',
                str(user_agent_parser.ParseUserAgent(submit.os)['family']),
                str(user_agent_parser.ParseOS(submit.os)['family'])
            ]

            answers = ANSWER.objects.filter(submit_id=submit.id)

            for answer in answers:
                if answer.type == 1:
                    if answer.is_null:
                        row.append('')
                    choice = A_CHOICE.objects.get(answer_id=answer.id)
                    row.append(choice.option.index)

                elif answer.type == 2:
                    choices = A_CHOICE.objects.filter(answer_id=answer.id)
                    optionsCount = Q_CHOICE.objects.filter(question_id=answer.question.id).count()
                    if answer.is_null:
                        for i in range(optionsCount):
                            row.append('')
                        continue

                    choicesArray = [0] * optionsCount
                    for choiceIndex, choice in enumerate(choices):
                        choicesArray[choice.option.index - 1] = 1
                    for choice in choicesArray:
                        row.append(choice)

                elif answer.type == 3:
                    if answer.is_null:
                        row.append('')
                    # noinspection PyBroadException
                    try:
                        completion = A_COMPLETION.objects.get(answer_id=answer.id)
                        row.append(completion.content)
                    except:
                        row.append('')

                elif answer.type == 7:
                    urls = ''
                    images = A_IMAGE.objects.filter(answer_id=answer.id)
                    for imgIndex, img in enumerate(images):
                        url = settings.IMAGES_URL + str(img.url)
                        urls += url if imgIndex == 0 else '┋' + url
                    row.append(urls)

            data.append(row)
    return codeMsg(20213, "项目数据导出成功", data)


@jsonLoad
# @tokenCheck
# @questionPermissionCheck
def getSubmitDetail(request):
    submitID = request.POST['submitID']
    submit = SUBMIT.objects.get(id=submitID)

    data = {
        'list': [],
        'submitID': submitID,
        'submitTime': submit.to_dict()['submit_time'],
        'ip': submit.ip
    }

    answers = ANSWER.objects.filter(submit_id=submitID)

    for answer in answers:
        question = {
            'questionID': answer.question.id,
            'questionTitle': answer.question.title
        }

        if answer.type == 1:
            question['answerID'] = A_CHOICE.objects.get(answer_id=answer.id).option.id
            question['answerText'] = A_CHOICE.objects.get(answer_id=answer.id).option.title

        elif answer.type == 2:
            question['answerID'] = []
            question['answerText'] = ''
            for choiceIndex, choice in enumerate(A_CHOICE.objects.filter(answer_id=answer.id)):
                question['answerID'].append(choice.option.id)
                question['answerText'] += choice.option.title if choiceIndex == 0 else '┋' + choice.option.title

        elif answer.type == 3:
            question['answerID'] = A_COMPLETION.objects.get(answer_id=answer.id).content
            question['answerText'] = question['answerID']

        data['list'].append(question)

    return codeMsg(20214, "问卷提交数据获取成功", data)


@jsonLoad
@tokenCheck
# @questionPermissionCheck
def deleteSubmit(request):
    data = {}
    submitID = request.POST['submitID']

    projectID = SUBMIT.objects.get(id=submitID).project_id
    # noinspection PyBroadException
    try:
        submit = SUBMIT.objects.get(id=submitID)
        submit.state = 0
        submit.save()

        project = PROJECT.objects.get(id=projectID)
        project.submits -= 1
        project.save()
    except:
        return codeMsg(20214, "问卷提交数据删除失败", data)
    return codeMsg(20214, "问卷提交数据删除成功", data)


@jsonLoad
def getRecommendations(request):
    data = []
    pageNumber = request.POST['pageNumber']

    projects = PROJECT.objects.select_related('user').filter(state=1)  # 这能减少SQL查询次数
    count = 8
    dictList = []
    for i in range(count):
        num = random.randint(0, projects.count() - 1)
        projectDict = model_to_dict(projects[num])
        projectDict['username'] = projects[num].user.username
        projectDict['imgNum'] = str(random.randrange(1, 60 + 1))
        dictList.append(projectDict)
    cardGroupData = {'type': 1, 'data': dictList}

    if pageNumber == 1:
        swipeData = {'type': 3, 'data': [
            {'title': '免费开源的问卷系统', 'imgUrl': 'undraw_friendship_mni7.svg'},
            {'title': '多端应用，随时随地收集问卷', 'imgUrl': 'undraw_before_dawn_re_hp4m.svg'},
            {'title': '界面简约，操作简单', 'imgUrl': 'undraw_explore_re_8l4v.svg'},
            {'title': '支持数据导出', 'imgUrl': 'undraw_romantic_getaway_re_3f45.svg'},
            {'title': '多种题型', 'imgUrl': 'undraw_tree_swing_re_pqee.svg'},
            {'title': '丰富的数据图表', 'imgUrl': 'undraw_romantic_getaway_re_3f45.svg'},
        ]}
        data.append(swipeData)
        data.append(cardGroupData)
        return codeMsg(20214, "问卷提交数据删除成功", data)
    else:
        project = getRandomQuerySetList(PROJECT.objects.filter(state=1), 1)

        boardData = {
            'type': 2,
            'data': {
                'id': project[0]['id'], 'title': project[0]['title'],
                'imgUrl': str(random.randrange(1, 60 + 1))
            }
        }
        data.append(cardGroupData)
        data.append(boardData)
        return codeMsg(20214, "问卷提交数据删除成功", data)


@jsonLoad
def searchProjects(request):
    keyword = request.POST['keyword']
    order = request.POST['order']
    page = request.POST['page']

    orderMode = {
        'default': 'submits',
        'submit': 'submits',
        'time': 'created_time'
    }
    pageItems = 10
    paginator = Paginator(
        PROJECT.objects.select_related('user').filter(state=1, title__icontains=keyword).order_by(
            orderMode[order]).reverse(),
        pageItems)
    projects = paginator.get_page(page)
    data = {'list': querySetToList(projects)}
    for itemIndex, item in enumerate(data['list']):
        del item['state']
        del item['end_time']
        item['imgUrl'] = str(random.randrange(1, 60 + 1))
        item['username'] = projects[itemIndex].user.username
        item['created_time'] = int(time.mktime(projects[itemIndex].created_time.timetuple()))
    data['numPages'] = paginator.num_pages
    return codeMsg(20214, "问卷提交数据删除成功", data)


def getHotProjects(request):
    pageItems = 20

    projects = PROJECT.objects.select_related('user').filter(state=1).order_by('-submits')[:pageItems]
    # projects = PROJECT.objects.filter(state=1).order_by('-submits')
    data = querySetToList(projects)
    for itemIndex, item in enumerate(data):
        del item['state']
        del item['end_time']
        item['imgUrl'] = str(random.randrange(1, 60 + 1))
        item['username'] = projects[itemIndex].user.username
        item['created_time'] = int(time.mktime(projects[itemIndex].created_time.timetuple()))

    return codeMsg(20214, "问卷提交数据删除成功", data)
