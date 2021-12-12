from django.http import HttpResponse
from send_mail.tasks import  send_mail_func
from django_celery_beat.models import PeriodicTask,CrontabSchedule

# Create your views here.
def send_mail_to_user(request):
    send_mail_func.delay()
    return HttpResponse("Task Completed celery beat")

def schedule_mail(request):
    schedule=CrontabSchedule.objects.create(hour=14,minute=35)
    try:
        PeriodicTask.objects.create(crontab=schedule,name='schedule_mail_'+'31'+'i',task="send_mail.tasks.send_mail_func")
    except:
            return HttpResponse("Already exist....")
    return HttpResponse("Done Scheduled task")
