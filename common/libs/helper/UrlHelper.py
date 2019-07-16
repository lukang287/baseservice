from application import app
import time


def buildUrl(path):
    return path


def buildStaticUrl(path):
    release_version = app.config.get('RELEASE_VERSION')
    ver = "%s" % (int(time.time())) if not release_version else release_version
    path = "/static" + path + "?ver=" + ver
    return buildUrl(path)