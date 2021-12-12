from django.urls import path
from . import views

urlpatterns = [
    path("",views.send_mail_to_user,name="send_mail_to_user"),
    path("schedule/",views.schedule_mail,name="schedule_mail"),
]
