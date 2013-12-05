from django.contrib import admin

from .models import UrlChecker

class UrlCheckerAdmin(admin.ModelAdmin):
    class Meta:
        model = UrlChecker
        
admin.site.register(UrlChecker, UrlCheckerAdmin)