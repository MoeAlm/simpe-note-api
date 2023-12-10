from django.contrib import admin
from notes_api import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Note)
