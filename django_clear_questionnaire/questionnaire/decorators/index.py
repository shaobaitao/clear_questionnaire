import json

from django.db.models import F, Max

from questionnaire.models import PROJECT, QUESTION
from tools.index import codeMsg
import re


def createCheck(f):
    """
    检查问卷项目格式
    """

    def wrap(request, *args, **kwargs):
        obj = json.loads(request.body)

        title = obj['title']
        desc = obj['desc']

        if re.match(r'^[\s\S]{1,100}$', title):
            if re.match(r'^[\s\S]{1,300}$', desc):
                return f(request, *args, **kwargs)
            return codeMsg(20402, "问卷欢迎语长度为1~300")
        return codeMsg(20401, "问卷标题长度为1~100")

    return wrap


def questionPermissionCheck(f):
    """
    检查是否有问题权限
    """

    def wrap(request, *args, **kwargs):
        id = request.payload['id']
        obj = json.loads(request.body)

        if id == PROJECT.objects.get(id=obj['projectID']).user_id:
            return f(request, *args, **kwargs)
        else:
            return codeMsg(20402, "没有题目权限")

    return wrap


def getQuestionsPublicCheck(f):
    """
    问卷问题数据公开获取合法性
    """

    def wrap(request, *args, **kwargs):
        projectID = request.POST['projectID']
        state = PROJECT.objects.get(id=projectID).state
        if state == 1:
            return f(request, *args, **kwargs)
        else:
            return codeMsg(20403, "问卷未发布")

    return wrap


def getQuestionsPrivateCheck(f):
    """
    问卷问题数据私有获取合法性
    """
    def wrap(request, *args, **kwargs):
        id = request.payload['id']
        obj = json.loads(request.body)

        if id == PROJECT.objects.get(id=obj['projectID']).user_id:
            return f(request, *args, **kwargs)
        else:
            return codeMsg(20402, "没有题目权限")

    return wrap


def questionSerialNumber(f):
    """
    返回问题的序号
    """

    def wrap(request, *args, **kwargs):
        questions = QUESTION.objects.filter(project=request.POST['projectID']).aggregate(Max('serial_number'))
        print(questions)
        if questions['serial_number__max'] is None:
            serialNumber = 1
        else:
            serialNumber = questions['serial_number__max'] + 1
        request.serialNumber = serialNumber
        return f(request, *args, **kwargs)

    return wrap


def radioCheck(f):
    """
    检查单选题格式
    """

    def wrap(request, *args, **kwargs):
        obj = json.loads(request.body)
        if len(obj['question']['title']) == 0 or len(obj['question']['options']) < 2:
            return codeMsg(20403, "题目标题不能为空，题目选项大于等于两个，题目选项标题不能为空")
        for i in obj['question']['options']:
            if len(i['title']) == 0:
                return codeMsg(20403, "题目标题不能为空，题目选项大于等于两个，题目选项标题不能为空")
        return f(request, *args, **kwargs)

    return wrap


def completionCheck(f):
    """
    检查填空题格式
    """

    def wrap(request, *args, **kwargs):
        obj = json.loads(request.body)
        if len(obj['question']['title']) == 0:
            return codeMsg(20404, "题目标题不能为空")

        return f(request, *args, **kwargs)

    return wrap
