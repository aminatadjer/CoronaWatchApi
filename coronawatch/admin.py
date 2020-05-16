from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import *
from customauth.models import User
# Register your models here.

admin.site.site_header = "Administration de CORONAWATCH"
admin.site.register(Publication)


admin.site.register(User)

admin.site.register(EtatSante)
admin.site.register(InformationsVirus)
admin.site.register(RebotSource)
admin.site.register(VideoInternaut)



admin.site.unregister(Group)