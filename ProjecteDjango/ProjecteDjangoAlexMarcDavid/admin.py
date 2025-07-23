from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Game, Platform
# Register your models here.
class GameAdmin(ModelAdmin):
    pass

admin.site.register(Game, ModelAdmin)


class PlatformAdmin(ModelAdmin):
    pass

admin.site.register(Platform, ModelAdmin)