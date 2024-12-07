# coding: utf-8
'''
official: https://learn.hayfrp.com/api.html
---
注意：在调用HayFrp OPENAPI时，请您务必加上标头Headers："waf: off"以绕过雷池防火墙.
主要API地址（CloudFlare减速云，支持From-data/JSON数据提交方式）：https://api.hayfrp.com
镜像API地址（国内加速，POST提交数据仅支持JSON格式传入）：https://hayfrpapi.rcov.top
注意：镜像API调用需授权，未授权无法调用镜像API，可以在QQ群找@Frush获取调用权限.
警告：禁止使用HayFrp OPENAPI进行任何违法操作，包括但不限于：非法获取他人CSRF并接管账号权限、非法调用OPENAPI进行邮箱发件等
在您使用HayFrp OPENAPI时，请务必标注HayFrp OPENAPI或其他字样，禁止标注对HayFrp OPENAPI不利字样。
使用HayFrp OPENAPI即代表您已同意协议。
镜像源API协议与主要API协议不同，请仔细阅读。
'''
import utils as u
from errors import *

class account:
    '''
    # First - 用户账号API
    该API下的全局路径为：/user
    全局请求方式：JSON
    全局请求类型：POST
    '''
    username = ''  # 用户名
    password = ''  # 密码
    csrf = ''  # 鉴权用 CSRF
    api_base = ''  # api 地址

    def __init__(self,
                 username: str = None,
                 password: str = None,
                 csrf: str = None,
                 api_base: str = 'https://api.hayfrp.com'
                 ) -> bool:
        '''
        初始化用户 class

        @param username: 用户名
        @param password: 密码 *(明文)*
        '''
        assert (username and password) or csrf, MissingParamError('需要 用户名/密码 或 csrf')