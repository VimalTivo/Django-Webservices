from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from datetime import datetime
from jsonfield import JSONField

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    # created = models.DateTimeField(auto_now_add=True)
    # title = models.CharField(max_length=100, blank=True, default='')
    # code = models.TextField()
    # linenos = models.BooleanField(default=False)
    # language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    # style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    ids = models.CharField(max_length=200, blank=True, default='')
    resource = models.CharField(max_length=200, blank=True, default='')
    operation = models.CharField(max_length=200, blank=True, default='')
    ref = JSONField(blank=True, default='')
    airdate = models.CharField(max_length=200, blank=True, default='')
    end_airdate = models.CharField(max_length=200, blank=True, default='')
    content = JSONField(blank=True, default='')
    source = JSONField(blank=True, default='')
    date = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        ordering = ('ids',)

class Snippet2(models.Model):
    resource = models.CharField(max_length=200, blank=True, default='')
    operation = models.CharField(max_length=200, blank=True, default='')
    ref = JSONField(blank=True, default='')
    airdate = models.CharField(max_length=200, blank=True, default='')
    end_airdate = models.CharField(max_length=200, blank=True, default='')
    content = JSONField(blank=True, default='')
    source = JSONField(blank=True, default='')
    date = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        ordering = ('date',)

class Snippet3(models.Model):
    resource = models.CharField(max_length=200, blank=True, default='')
    operation = models.CharField(max_length=200, blank=True, default='')
    ref = JSONField(blank=True, default='')
    airdate = models.CharField(max_length=200, blank=True, default='')
    end_airdate = models.CharField(max_length=200, blank=True, default='')
    content = JSONField(blank=True, default='')
    source = JSONField(blank=True, default='')
    date = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        ordering = ('date',)

class Snippet4(models.Model):
    resource = models.CharField(max_length=200, blank=True, default='')
    operation = models.CharField(max_length=200, blank=True, default='')
    ref = JSONField(blank=True, default='')
    airdate = models.CharField(max_length=200, blank=True, default='')
    end_airdate = models.CharField(max_length=200, blank=True, default='')
    content = JSONField(blank=True, default='')
    source = JSONField(blank=True, default='')
    date = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        ordering = ('date',)

class Snippet5(models.Model):
    resource = models.CharField(max_length=200, blank=True, default='')
    operation = models.CharField(max_length=200, blank=True, default='')
    ref = JSONField(blank=True, default='')
    airdate = models.CharField(max_length=200, blank=True, default='')
    end_airdate = models.CharField(max_length=200, blank=True, default='')
    content = JSONField(blank=True, default='')
    source = JSONField(blank=True, default='')
    date = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        ordering = ('date',)

class Snippet6(models.Model):
    resource = models.CharField(max_length=200, blank=True, default='')
    operation = models.CharField(max_length=200, blank=True, default='')
    ref = JSONField(blank=True, default='')
    airdate = models.CharField(max_length=200, blank=True, default='')
    end_airdate = models.CharField(max_length=200, blank=True, default='')
    content = JSONField(blank=True, default='')
    source = JSONField(blank=True, default='')
    date = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        ordering = ('date',)

class Snippet7(models.Model):
    resource = models.CharField(max_length=200, blank=True, default='')
    operation = models.CharField(max_length=200, blank=True, default='')
    ref = JSONField(blank=True, default='')
    airdate = models.CharField(max_length=200, blank=True, default='')
    end_airdate = models.CharField(max_length=200, blank=True, default='')
    content = JSONField(blank=True, default='')
    source = JSONField(blank=True, default='')
    date = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        ordering = ('date',)

class Snippet8(models.Model):
    resource = models.CharField(max_length=200, blank=True, default='')
    operation = models.CharField(max_length=200, blank=True, default='')
    ref = JSONField(blank=True, default='')
    airdate = models.CharField(max_length=200, blank=True, default='')
    end_airdate = models.CharField(max_length=200, blank=True, default='')
    content = JSONField(blank=True, default='')
    source = JSONField(blank=True, default='')
    date = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        ordering = ('date',)

class Snippet9(models.Model):
    resource = models.CharField(max_length=200, blank=True, default='')
    operation = models.CharField(max_length=200, blank=True, default='')
    ref = JSONField(blank=True, default='')
    airdate = models.CharField(max_length=200, blank=True, default='')
    end_airdate = models.CharField(max_length=200, blank=True, default='')
    content = JSONField(blank=True, default='')
    source = JSONField(blank=True, default='')
    date = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        ordering = ('date',)

class Snippet10(models.Model):
    resource = models.CharField(max_length=200, blank=True, default='')
    operation = models.CharField(max_length=200, blank=True, default='')
    ref = JSONField(blank=True, default='')
    airdate = models.CharField(max_length=200, blank=True, default='')
    end_airdate = models.CharField(max_length=200, blank=True, default='')
    content = JSONField(blank=True, default='')
    source = JSONField(blank=True, default='')
    date = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        ordering = ('date',)


class Key_Secret(models.Model):
    key = models.TextField(max_length=200, blank=False, unique=True,default=None)
    secret = models.TextField(max_length=200, blank=False,unique=True,default=None)
    class Meta:
        ordering = ('key',)
