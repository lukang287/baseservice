# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache
import os


class Application( Flask ):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(import_name, template_folder=template_folder, root_path=root_path, static_folder=None)
        self.config.from_pyfile('config/base_config.py')
        if "ops_config" in os.environ:
            self.config.from_pyfile( 'config/production_config.py')
        else:
            self.config.from_pyfile('config/local_config.py')
        db.init_app(self)
        cache.init_app(self)


db = SQLAlchemy()
cache = Cache()
app = Application(__name__, template_folder=os.getcwd()+"/web/templates/", root_path=os.getcwd())
manager = Manager(app)

#log


'''
函数模板
'''
# from common.libs.UrlManager import UrlManager
# app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
# app.add_template_global(UrlManager.buildUrl, 'buildUrl')
# app.add_template_global(UrlManager.buildImageUrl, 'buildImageUrl')


