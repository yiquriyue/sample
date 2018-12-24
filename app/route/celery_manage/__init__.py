from flask import Blueprint
celery_manage = Blueprint('celery_manage', __name__)
from . import views