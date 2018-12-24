# -*- coding: utf-8 -*-
#!/usr/bin/env python

from app import app
from flask_script import Manager, Server
from gevent import pywsgi
from gevent import monkey


monkey.patch_all()
manager = Manager(app)

@manager.command
def runserver():
    print "server start at %s:%d"%("172.31.50.254",5000)
    http_server = pywsgi.WSGIServer(("172.31.50.254",5000), app)
    http_server.serve_forever()
if __name__ == '__main__':
    manager.run()