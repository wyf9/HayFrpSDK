# coding: utf-8

class HayFrpSDKBaseException(Exception):
    '''
    Base Exception
    '''

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class MissingParamException(HayFrpSDKBaseException):
    '''
    传入参数不足
    '''

# --- 下面是根据 api 返回设置的异常

class MissingDataException(HayFrpSDKBaseException):
    '''
    数据缺失
    status: 404
    message: XXX不能为空.
    '''

class MissingTypeException(HayFrpSDKBaseException):
    '''
    未指定操作(type值未设置)
    status: 404
    message: 无用户类型.
    '''

class WrongPasswdException(HayFrpSDKBaseException):
    '''
    密码错误
    status: 403
    message: 登录失败，您的密码有误.
    '''

class UserNotFoundException(HayFrpSDKBaseException):
    '''
    用户不存在
    status: 404
    message: 用户还没有注册.
    '''