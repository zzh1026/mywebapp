#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2018/3/21

__author__ = 'zzh'

#
# 测试 在 awesome 数据库的 user 表中添加数据 ,主要用来测试是否能连通 mysql 数据库
#

import asyncio

import orm
from models import User


async def test(loop):
    # 创建连接池
    await orm.create_pool(loop=loop, user='root', password='wszzh19921026', db='awesome')
    u = User(name='zzh', email='zzh@163.com', passwd='1234567890', image='about:blank')
    await u.save()
    await orm.close_pool()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
