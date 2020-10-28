
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


#######################  这一坨配置是为了让外部脚本使用 django orm ######################
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "whisper.settings")
sys.path.append(os.path.abspath(os.path.join(BASE_DIR, os.pardir)))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


#######################  正式部分 ######################

from core.models import Message

msg = Message.objects.all()
print(msg)