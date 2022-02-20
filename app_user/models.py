from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from resume.models import Resume


class AppUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	account_type = models.CharField(default="candidate",max_length=10)

	cprofile_status = models.BooleanField(default=False)
	profile_photo = models.FileField(upload_to='account_files/profile_photos/', blank=True, default="default_files/default_face.png")
	address = models.TextField(default=" ")
	country = models.CharField(default=" ",max_length=20)
	phone_no = models.CharField(default=" ",max_length=10)
	age = models.IntegerField(null=True)

	#socials
	facebook_link = models.CharField(default="#",max_length=10)
	twitter_link = models.CharField(default="#",max_length=10)
	instagram_link = models.CharField(default="#",max_length=10)
	whatsapp_link = models.CharField(default="#",max_length=10)
	github_link = models.CharField(default="#",max_length=10)


	#recruiters
	agency_name = models.CharField(default="",max_length=30)
	agency_logo = models.FileField(upload_to='account_files/profile_photos/', blank=True, default="default_files/default_face.png")

	
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True)

	otp_code = models.CharField(default="none",max_length=10)
	
	ec_status = models.BooleanField(default=False)
	status = models.BooleanField(default=False)
	
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.username