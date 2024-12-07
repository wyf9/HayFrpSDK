# coding: utf-8

class MissingParamError(Exception):
    '''
    传入参数不足
    '''
    def __init__(self, msg):
         self.msg = msg

    def __str__(self):
        return f'传入参数不足: {self.msg}'