from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from API.settings import EMAIL_HOST_USER
# Create your views here.


def send(_message, _subject, _media, _receivers):
    message = _message
    subject = _subject
    email = EmailMessage(subject, message, EMAIL_HOST_USER, _receivers)
    email.attach_file(_media)
    email.send()
