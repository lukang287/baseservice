# -*- coding: utf-8 -*-
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'mysql://db_admin:lukang11@cdb-dsfuxk31.gz.tencentcdb.com:10067/onelearn?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8mb4"

CACHE_MEMCACHED_SERVERS=['111.230.248.221:11211']
CACHE_TYPE='memcached'
CACHE_DEFAULT_TIMEOUT=120

APP = {
    'app_name': 'One自习测试',
    'app_version': '1.0',
    'api_domain': 'http://127.0.0.1:9000',
    'pay_domain': 'https://api.eantec.cn/api',
    'resource_domain': 'http://94.191.49.241'
}

FTP_CONFIG = {
    'host': '94.191.49.241',  #
    'port': 21,
    'user': 'ftpadmin',
    'passwd': 'ftpadmin',
    'local_dir': '',
    'server_dir': ''
}
