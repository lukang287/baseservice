# -*- coding: utf-8 -*-
import json

from flask import Blueprint, request, redirect, jsonify
from application import app, db
from common.libs.helper.DateTimeHelper import get_str_now
from common.libs.helper.SecureHelper import gen_salt, gen_auth_code
from common.libs.weixin.WXBizDataCrypt import WXBizDataCrypt
from common.libs.weixin.weixinHelper import getWeChatInfoByCode
from common.models.member.Member import Member
from common.models.member.OauthMemberBind import OauthMemberBind


route_member = Blueprint('member_page', __name__)


@route_member.route("/member/wx_login", methods=["GET", "POST"])
def login():
    """
    @api {post} /member/wx_login 小程序用户登录
    @apiVersion 1.0.0
    @apiGroup wxUser
    @apiName login
    @apiParam {String}  code      (必须)    微信返回的code
    @apiParam {String}  encryptedData      (必须)    微信返回的加密数据
    @apiParam {String}  iv      (必须)    微信返回的初始向量
    @apiParamExample {json} Request-Example:
    {
        code: "13970512239",
        encryptedData: "sdfasdfsdfewerwq23123",
        iv: "21asdasdaqwe"
    }
    @apiSuccess (回参) {String} token  用户token
    @apiSuccessExample {json} Success-Response:
    {
        "code":200,
        "msg":"操作成功",
        "data": {
            "token": "13813888888#1",
        }
    }
    @apiErrorExample {json} Error-Response:
    {
        "code":-1,
        "msg":"登录失败"
    }
    """
    resp = {'code':200, 'msg':'操作成功~', 'data':{}}
    req = request.values
    code = req['code'] if 'code' in req else ''
    encryptedData = req['encryptedData'] if 'encryptedData' in req else ''
    iv = req['iv'] if 'iv' in req else ''
    if not code or len(code) < 1:
        resp['code'] = -1
        resp['msg'] = "需要code"
        return jsonify(resp)

    openid, session_key, unionid = getWeChatInfoByCode(code)
    if openid is None:
        resp['code'] = -1
        resp['msg'] = "调用微信出错"
        return jsonify(resp)

    try:
        wxapp = WXBizDataCrypt(app.config['MINA_APP']['appid'], session_key)
        user_info = wxapp.decrypt(encryptedData, iv)
        print(user_info)
        nickname = user_info['nickName'] if 'nickName' in user_info else ''
        sex = user_info['gender'] if 'gender' in user_info else 0
        avatar = user_info['avatarUrl'] if 'avatarUrl' in user_info else ''
        province = user_info['province'] if 'province' in user_info else ''
        city = user_info['city'] if 'city' in user_info else ''
    except Exception:
        resp['code'] = -1
        resp['msg'] = '获取用户信息失败，请重新登录'
        return jsonify(resp)

    #判断是否已经测试过，注册了直接返回一些信息
    bind_info = OauthMemberBind.query.filter_by(openid=openid, type=1).first()
    if not bind_info:
        model_member = Member()
        model_member.nickname = nickname
        model_member.sex = sex
        model_member.avatar = avatar
        model_member.province = province
        model_member.city = city
        model_member.salt = gen_salt()
        model_member.reg_ip = request.remote_addr
        model_member.updated_time = model_member.created_time = ()
        db.session.add(model_member)
        db.session.commit()

        model_bind = OauthMemberBind()
        model_bind.member_id = model_member.id
        model_bind.client_type = 'weixin'
        model_bind.type = 1 #weixin
        model_bind.openid = openid
        model_bind.unionid = unionid
        model_bind.session_key = session_key
        model_bind.extra = json.dumps(user_info)
        model_bind.updated_time = model_bind.created_time = get_str_now()
        db.session.add(model_bind)
        db.session.commit()

        bind_info = model_bind

        #创建用户账户，发注册礼物

    member_info = Member.query.filter_by(id=bind_info.member_id).first()
    token = "%s#%s" % (gen_auth_code(member_info), member_info.id)
    resp['data'] = {'token': token}
    return jsonify(resp)


@route_member.route("/member/check_reg", methods=["GET", "POST"])
def checkReg():
    """
        @api {post} /member/check_reg 检查用户是否已授权登录
        @apiVersion 1.0.0
        @apiGroup wxUser
        @apiName check_reg
        @apiParam {String}  code      (必须)    微信返回的code
        @apiParamExample {json} Request-Example:
        {
            code: "13970512239"
        }
        @apiSuccess (回参) {String} token  用户token
        @apiSuccessExample {json} Success-Response:
        {
            "code":200,
            "msg":"操作成功",
            "data": {
                "token": "13813888888",
            }
        }
        @apiErrorExample {json} Error-Response:
        {
            "code":-1,
            "msg":"未查询到绑定信息"
        }
        """
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    code = req['code'] if 'code' in req else ''
    if not code or len(code) < 1:
        resp['code'] = -1
        resp['msg'] = "需要code"
        return jsonify(resp)

    openid, session_key, unionid = getWeChatInfoByCode(code)
    if openid is None:
        resp['code'] = -1
        resp['msg'] = "调用微信出错"
        return jsonify(resp)

    bind_info = OauthMemberBind.query.filter_by(openid=openid, type=1).first()
    if not bind_info:
        resp['code'] = -1
        resp['msg'] = "未绑定"
        return jsonify(resp)

    member_info = Member.query.filter_by(id=bind_info.member_id).first()
    if not member_info:
        resp['code'] = -1
        resp['msg'] = "未查询到绑定信息"
        return jsonify(resp)

    token = "%s#%s"%(gen_auth_code(member_info), member_info.id)
    resp['data'] = {'token': token}
    return jsonify(resp)
