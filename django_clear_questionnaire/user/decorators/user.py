import json
import re
import time
import jwt

from django.conf import settings

from tools.index import codeMsg


def jsonLoad(f):
    """
    request.POST = json.loads(request.body)
    """

    def wrap(request, *args, **kwargs):
        request.POST = json.loads(request.body)
        return f(request, *args, **kwargs)

    return wrap


def emailCheck(f):
    """
    检查邮箱格式
    """

    def wrap(request, *args, **kwargs):
        request.POST = json.loads(request.body)
        email = request.POST['email']
        if re.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', email) is not None:
            return f(request, *args, **kwargs)
        return codeMsg(10401, '邮箱格式验证失败')

    return wrap


def passwordCheck(f):
    """
    检查密码格式 必须64位16进制串
    """

    def wrap(request, *args, **kwargs):
        request.POST = json.loads(request.body)
        password = request.POST['password']
        if re.match(r'^\w{64}$', password) is not None:
            return f(request, *args, **kwargs)
        return codeMsg(10402, '密码格式验证失败')

    return wrap


def accountCheck(f):
    """
    检查账号格式 账号可能是用户名、邮箱、手机号其中之一
    """

    def wrap(request, *args, **kwargs):
        request.POST = json.loads(request.body)
        username = request.POST.get('username')
        # 账号任意字符1~20位即可
        # 这里邮箱的位数可能会超过20
        if re.match(r'^[\s\S]{1,40}$', username):
            return f(request, *args, **kwargs)
        return codeMsg(10403, '账号格式错误')

    return wrap


def generateToken(id: str) -> str:
    """
    生成Token
    """
    dic = {
        'id': id,
        'exp': time.time() + settings.TOKEN_EXPIRE
    }
    token = jwt.encode(dic, settings.TOKEN_SALT, 'HS256')
    print(token)
    return token


def tokenCheck(f):
    """
    解析Token
    """

    def wrap(request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return codeMsg(10404, '未携带Token')
        # noinspection PyBroadException
        try:
            request.payload = jwt.decode(token, settings.TOKEN_SALT, 'HS256')
        except Exception as e:
            print(e)
            return codeMsg(10405, 'Token解析失败')
        return f(request, *args, **kwargs)

    return wrap


def usernameCheck(f):
    """
    检查用户名格式
    """

    def wrap(request, *args, **kwargs):
        request.POST = json.loads(request.body)
        newUsername = request.POST.get('newUsername')
        # 账号任意字符1~20位即可
        if (not re.match(r'^\w{1,20}$', newUsername)) or \
                newUsername.find('@') or \
                newUsername.find('qw_') or \
                '0' <= newUsername[0] <= '9':
            return f(request, *args, **kwargs)
        return codeMsg(10411, '用户名格式错误')

    return wrap
