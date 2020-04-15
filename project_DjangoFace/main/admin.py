from django.contrib import admin
from .models import Suspect
# Register your models here.


from django.apps import AppConfig

class MainConfig(AppConfig):
    name = 'main'
    verbose_name = "Сотрудник"


@admin.register(Suspect)

class UserAdmin(admin.ModelAdmin):
    list_display = ['author','surname', 'name', 'patronymic']


