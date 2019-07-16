# -*- coding: utf-8 -*-
from application import app
from flask import request, jsonify

@app.errorhandler(403)
def error_403(e):
    path = request.path
    if 'api/' in path:
        # AppLogService.addErrorLog(str(e))
        pass
    return jsonify({'code': 403, 'reason': '请求异常，请稍后再试'})
