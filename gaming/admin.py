from django.contrib import admin
from .models import Newbie, Pro, Submitter
# Register your models here.

admin.site.register(Submitter)
admin.site.register(Newbie)
admin.site.register(Pro)