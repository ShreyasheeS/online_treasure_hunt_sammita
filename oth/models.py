from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class player(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=128)
	max_level = models.IntegerField(default = 1)

	def __unicode__(self):
		return self.name

class level(models.Model):
	l_number = models.IntegerField()
	#photo = models.ImageField(upload_to='/static/images/')
	text = models.TextField()
	answer = models.CharField(max_length=200)

	def __unicode__(self):
		return self.text

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username


admin.site.register(player)
admin.site.register(level)
admin.site.register(UserProfile)
