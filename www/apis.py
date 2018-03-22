#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2018/3/21

__author__ = 'zzh'

'''
JSON API definition.
'''


class APIError(Exception):
    '''
    自定义的APIError基类, error 必传 , data 和 message 可选
    '''

    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message


class APIValueError(APIError):
    '''
    输入值有错误或无效。数据指定输入表单的错误字段。
    '''

    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)


class APIResourceNotFoundError(APIError):
    '''
    资源找不到, 数据指定资源名.
    '''

    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound', field, message)


class APIPermissionError(APIError):
    '''
    api没有权限
    '''

    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)
