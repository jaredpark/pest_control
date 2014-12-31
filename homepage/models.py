from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	address = models.CharField(default='',blank=True, max_length=60)
	city = models.CharField(default='',blank=True, max_length=20)
	zipcode = models.IntegerField(default=85111,blank=True, max_length=5)
	phone = models.CharField(default='',blank=True, max_length=11)

	def __unicode__(self):
		return(self.user.username)

