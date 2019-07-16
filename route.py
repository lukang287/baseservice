# -*- coding: utf-8 -*-
from application import app

'''
统一拦截处理和统一错误处理
'''
from web.aop.ApiAuthInterceptor import *
from web.aop.ErrorInterceptor import *

'''
蓝图功能，对所有的url进行蓝图功能配置
'''
from web.api.index.Index import route_index

app.register_blueprint(route_index, url_prefix="/api")

