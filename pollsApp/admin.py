from django.contrib import admin

# Register your models here.
from pollsApp.models import Client, Question, Choice

admin.site.register(Client)
admin.site.register(Question)
admin.site.register(Choice)