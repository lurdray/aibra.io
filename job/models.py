from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from interview.models import Interview
from quiz.models import Quiz, Result
from app_user.models import AppUser




class Answer(models.Model):
	app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)

	question_id = models.CharField(max_length=50, default="None")
	answer = models.CharField(max_length=50, default="None")
	
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.answer



class Application(models.Model):
	app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)

	answers = models.ManyToManyField(Answer, through="ApplicationAnswerConnector")

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.app_user



class Job(models.Model):
	title = models.CharField(max_length=20, default="none")
	salary = models.CharField(max_length=20, default="none")
	category = models.CharField(max_length=30, default="none")
	description = models.TextField(default="none")
	
	job_type = models.CharField(max_length=10, default="none")
	responsibility = models.TextField(default="none")
	requirement = models.TextField(default="none")
	contact_phone = models.CharField(max_length=20, default="none")
	contact_email = models.CharField(max_length=30, default="none")

	address = models.TextField(default="none")
	country = models.CharField(max_length=30, default="none")

	deadline = models.CharField(max_length=30, default="none")
	#deadline = models.DateTimeField(default=timezone.now)

	app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)

	applications = models.ManyToManyField(Application, through="JobApplicationConnector")
	interviews = models.ManyToManyField(Interview, through="JobInterviewConnector")
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
	results = models.ManyToManyField(Result, through="JobResultConnector")



	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title


class JobRequest(models.Model):
	app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	title = models.CharField(max_length=20, default="none")
	description = models.TextField(default="none")
	salary = models.CharField(max_length=20, default="none")
	job_type = models.CharField(max_length=20, default="none")
	slots = models.CharField(max_length=20, default="none")
	deadline = models.CharField(max_length=30, default="none")

	fulfills = models.ManyToManyField(Job, through="JobRequestJobConnector")
	
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

class ApplicationAnswerConnector(models.Model):
	application = models.ForeignKey(Application, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)




class JobResultConnector(models.Model):
	job = models.ForeignKey(Job, on_delete=models.CASCADE)
	result = models.ForeignKey(Result, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)




class JobApplicationConnector(models.Model):
	job = models.ForeignKey(Job, on_delete=models.CASCADE)
	application = models.ForeignKey(Application, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)



class JobInterviewConnector(models.Model):
	job = models.ForeignKey(Job, on_delete=models.CASCADE)
	interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)



class JobRequestJobConnector(models.Model):
	job_request = models.ForeignKey(JobRequest, on_delete=models.CASCADE)
	job = models.ForeignKey(Job, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)
