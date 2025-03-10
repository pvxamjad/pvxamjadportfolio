from django.contrib import admin
from portfolio.models import *

admin.site.register(Category)
admin.site.register(protfolio)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')

admin.site.register(Contact,ContactAdmin)



