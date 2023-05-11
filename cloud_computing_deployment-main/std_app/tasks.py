from django.conf import settings
from Homeapp.models import Borrowedbooks
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
 
from celery import shared_task
from celery.utils.log import get_task_logger
 
logger = get_task_logger(__name__)
 
@shared_task()
def thirty_second_func():
    logger.info("I run every 30 seconds using Celery Beat")
    return "Done"
 
@shared_task()
def notify():
    set = Borrowedbooks.objects.all()
    for x in set:
        subject = f"Notice to return { x.bks_id.book_title }"
        message = f"Dear { x.std_number.stdname }, \nYou are hear by being remindered that you are left with only day to the return \n{x.bks_id.book_title}" 
        if timezone.now() == (x.borrow_date + timezone.timedelta(days = 2)):
            send_mail(subject, message, settings.EMAIL_HOST_USER, [x.std_number.email,])
    logger.info("notify me please")
    return 'done'