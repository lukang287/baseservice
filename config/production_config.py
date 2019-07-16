# -*- coding: utf-8 -*-
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'mysql://db_admin:lukang11@cdb-dsfuxk31.gz.tencentcdb.com:10067/onelearn?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8mb4"

CACHE_MEMCACHED_SERVERS=['127.0.0.1:11211']
CACHE_TYPE='memcached'
CACHE_DEFAULT_TIMEOUT=120

RELEASE_VERSION="20181124001"

APP = {
    'app_name': 'One自习',
    'app_version': '1.0',
    'api_domain': 'https://api.eantec.cn/api',
    'pay_domain': 'https://api.eantec.cn/callback',
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