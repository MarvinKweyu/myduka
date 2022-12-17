import os

from celery import Celery

# django settings module for prog
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myduka.settings")
app = Celery("myduka")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
