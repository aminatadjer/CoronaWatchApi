from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from API.settings import EMAIL_HOST_USER
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
# Create your views here.


def send(_message, _subject, _media, _receivers):
    message = _message
    subject = _subject
    html_message = render_to_string(
        'email_template.html', {'Commentaire': message})
    plain_message = strip_tags(html_message)
    email = EmailMultiAlternatives(subject, plain_message, EMAIL_HOST_USER,
                                   _receivers)
    email.attach_alternative(html_message, "text/html")
    email.attach_file(_media)
    email.send()
