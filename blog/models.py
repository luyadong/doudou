#coding:utf8
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    msg = models.CharField(max_length=30)
    headImg = models.FileField(upload_to='upload/')

    user = models.ForeignKey(User, unique=True)

class Reply(models.Model):
    content = models.TextField(max_length=500)
    date = models.DateTimeField()
    user = models.ForeignKey(UserProfile)
    
    def __unicode__(self):
	return self.content[0:50]

class Blog(models.Model):
    title = models.CharField(verbose_name=u'标题', max_length=30)
    type = models.CharField(verbose_name=u'类型', max_length=1, choices=(('y','原创'),('z','转载'),('f','翻译')))
    pub_date = models.DateTimeField()
    author = models.ForeignKey(UserProfile)
    digest = models.CharField(verbose_name=u'博文摘要', max_length=100)
    content = models.TextField(verbose_name=u'博文内容', max_length=20000)
    picture  = models.FileField(verbose_name='图片附件',upload_to='Picture/')
    reply = models.ForeignKey(Reply)

    def __unicode__(self):
        return self.title

