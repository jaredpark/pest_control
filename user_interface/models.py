from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from registration.signals import user_registered

class UserProfile(models.Model):
	# user = models.OneToOneField(User)
	user = models.ForeignKey(User, unique=True)
	first_name = models.CharField(default='',blank=False, max_length=20)
	last_name = models.CharField(default='',blank=False, max_length=20)
	address = models.CharField(default='',blank=True, max_length=60)
	city = models.CharField(default='',blank=True, max_length=20)
	zipcode = models.IntegerField(default=85111,blank=False, max_length=5)
	phone = models.CharField(default='',blank=True, max_length=12)
	email = models.EmailField(default='',blank=True, max_length=40)
	next_appointment = models.DateTimeField(blank=True)
	balance = models.DecimalField(default=0.0,blank=True,max_digits=6,decimal_places=2)
	dog = models.BooleanField(blank=True)
	public = models.BooleanField(default=False,blank=True)
	notes = models.TextField(default='',blank=True,max_length=200)

	class Meta:
		verbose_name = _('user profile')
		verbose_name_plural = _('user profiles')

	def __unicode__(self):
		return(self.user.username)

	def attrs(self):
		out = []
		for field in self._meta.fields:
			out.extend([field.name, getattr(self, field.name)])
		return(out)

	def user_registered_callback(sender, user, request, **kwargs):
		profile = UserProfile(user = user)
		profile.first_name = request.POST["first_name"]
		profile.last_name = request.POST["last_name"]
		profile.email = request.POST["email"]
		profile.zipcode = int(request.POST["zipcode"])
		profile.save()
		user.first_name = request.POST["first_name"]
		user.last_name = request.POST["last_name"]
		user.email = request.POST["email"]
		user.save()
 
	user_registered.connect(user_registered_callback)