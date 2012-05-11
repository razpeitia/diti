from django.contrib import admin
from main.models import Page, Slide

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    

admin.site.register(Page, PageAdmin)
admin.site.register(Slide)