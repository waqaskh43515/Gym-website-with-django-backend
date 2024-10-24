from django.contrib import admin
from . models import Videos


class VideosAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Message')


admin.site.register(Videos, VideosAdmin)

# Register your models here.
