# -*- coding: utf-8 -*-
#!/usr/bin/env python
from flask import Flask
from flask_apscheduler import APScheduler
from flask import  render_template
scheduler=APScheduler()
app = Flask(__name__)
app.config.from_object('appconfig.Config')
# yiquriyue(yiquriyue@outlook.com):初始化定时任务，开启定时任务
scheduler.init_app(app)
scheduler.start()

from app.route.celery_manage import celery_manage as celery_manage_blueprint
app.register_blueprint(celery_manage_blueprint)

@app.route('/')
def index():
    return render_template('index.html', title="Welcome")