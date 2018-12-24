# _*_ coding: utf-8 _*_
class Config(object):
    # 调试模式是否开启
    DEBUG = True
    # 多线程
    threaded = True
    # 定时任务的配置
    JOBS = [ { 'id': 'createschuler_job', 'func': 'app.route.celery_manage.views:import_data', 'args': None, 'trigger': 'interval', 'seconds': 10 } ]