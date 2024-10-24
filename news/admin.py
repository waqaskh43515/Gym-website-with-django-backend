from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Message','new_image')



admin.site.register(News, NewsAdmin)

