from django.contrib import admin
from django.db import models
from .models import Person, Music

# Register your models here.
admin.site.register(Person)
admin.site.register(Music)