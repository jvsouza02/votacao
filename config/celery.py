from celery import Celery

app = Celery(
    'votacao',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/1',
    include=['src.tasks.voto_task']
)

app.conf.update(
    timezone='America/Fortaleza',
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json'
)
