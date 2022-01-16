from datetime import date

from celery.task.schedules import crontab
from celery.decorators import periodic_task

from api.models import Chat, Schedule


@periodic_task(run_every=(crontab(hour=9-20, minute=0, day_of_week='*')))
def send_chat():
    chat_ids = Schedule.objects.filter(
        chat__status='NEW',
        sending_date=date.today()
    ).values_list('chat', flat=True)[:90]
    
    chats = Chat.objects.filter(pk__in=chat_ids)
    for chat in chats:
        chat.status = 'SENT'
    Chat.objects.bulk_update(chats, ['status'])
