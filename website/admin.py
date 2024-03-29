from django.contrib import admin
from website.models import contact, NewsLetter
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email', 'subject', 'message', 'created_date')
    list_filter = ('email','created_date')
    search_fields = ('name','message')

admin.site.register(contact,ContactAdmin)
admin.site.register(NewsLetter)