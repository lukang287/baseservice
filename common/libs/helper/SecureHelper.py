import hashlib
import random, string


def gen_salt(length=16):
    keylist = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
    return "".join(keylist)


def gen_auth_code(member_info=None):
    '''生成小程序授权码'''
    m = hashlib.md5()
    str = "%s-%s-%s" % (member_info.id, member_info.salt, member_info.status)
    m.update(str.encode("utf-8"))
    return m.hexdigest()