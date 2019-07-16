# -*- coding: utf-8 -*-
from application import app
from flask import request, g, jsonify
# from common.models.member.Member import Member
# from common.libs.UserHelper import geneAuthCode2
import re


@app.before_request
def before_request_api():
    """
    api认证
    """
    api_ignore_login_urls = app.config['API_IGNORE_LOGIN_URLS']

    path = request.path
    if '/api' not in path:
        return

    # AppLogService.addAccessLog()
    pattern = re.compile('%s' % "|".join(api_ignore_login_urls))
    if pattern.match(path):
        return

    member_info = check_member_login()
    g.member_info = None
    if member_info:
        g.member_info = member_info

    if not member_info:
        resp = {'code': -2, 'msg': '未登录~', 'data': {}}
        return jsonify(resp)

    return


def check_member_login():
    """
    判断用户是否已经登录
    """
    #auth_cookie = request.headers.get("Authorization")
    #print('auth cookie ', auth_cookie)
    auth_cookie = '13abe5b9b9809b57592d65e8591b15ea#6'

    if auth_cookie is None:
        return False

    auth_info = auth_cookie.split("#")
    if len(auth_info) != 2:
        return False

    try:
        member_info = Member.query.filter_by(id=auth_info[1]).first()
    except Exception:
        return False

    if member_info is None:
        return False

    if auth_info[0] != geneAuthCode2(member_info):
        return False

    if member_info.status != 1:
        return False

    return member_info
