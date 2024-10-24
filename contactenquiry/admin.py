from django.contrib import admin
from . models import Contactenquiry
# Register your models here.


class ContactenquiryAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Phone', 'Email', 'Message')

admin.site.register(Contactenquiry, ContactenquiryAdmin)