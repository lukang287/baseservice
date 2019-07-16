# -*- coding: utf-8 -*-
SERVER_PORT = 9000
DEBUG = False
SQLALCHEMY_ECHO = False

AUTH_COOKIE_NAME = "one_learn"

SEO_TITLE = "One自习"

API_IGNORE_LOGIN_URLS = [
    "/api/index",
    "/api/home/index",
    "/api/member/wx_login",
    "/api/member/check_reg",
    "/api/product/package_list",
    "/api/invite_group/get_rules",
    "/api/learn_race/get_rules",
    "/api/learn_race/get_list",
    "/api/page/business_rules",
    "/api/page/faq",
    "/api/order/callback"
]

UPLOAD = {
    'ext': ['jpg', 'gif', 'bmp', 'jpeg', 'png'],
    'prefix_path': '/web/static/upload/',
    'prefix_url': '/static/upload/'
}