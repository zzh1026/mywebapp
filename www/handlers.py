#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2018/3/21

__author__ = 'zzh'

'添加URL处理函数'
from coroweb import get, post
from models import User, Comment, Blog, next_id
import re, time, json, logging, hashlib, base64, asyncio


@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }
