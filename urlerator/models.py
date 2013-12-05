from django.db import models
from django.contrib.auth.models import User

class UrlChecker(models.Model):
    from_address = models.CharField(max_length=250, null=True, blank=True)
    to_address = models.CharField(max_length=250, null=True, blank=True)
    url_output = models.CharField(max_length=600, null=True, blank=True)
    html_output = models.CharField(max_length=700, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __unicode__(self, ):
        return self.from_address