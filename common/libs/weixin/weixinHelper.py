import requests, json
from application import app


def getWeChatInfoByCode(code):
    url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code" \
        .format(app.config['MINA_APP']['appid'], app.config['MINA_APP']['appkey'], code)
    r = requests.get(url)
    res = json.loads(r.text)
    openid, session_key, unionid = None, None, None
    session_key = None
    if 'openid' in res:
        openid = res['openid']
    if 'session_key' in res:
        session_key = res['session_key']
    if 'unionid' in res:
        unionid = res['unionid']
    return openid, session_key, unionid