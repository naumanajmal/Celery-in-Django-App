import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CELERY.settings')
app = Celery('CELERY')
app.autodiscover_tasks()
app.config_from_object('django.conf:settings', namespace='CELERY')
@app.task(bind = True)
def debug_task(self):
    print(f'Request:{self.request!r}')