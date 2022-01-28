from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.core.mail import send_mail

from datetime import datetime
import datetime as dt
import requests

from job.models import *
from app_user.models import AppUser

#from .forms import UserForm





def IndexView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		jobs = Job.objects.all()

		context = {"app_user": app_user, "jobs": jobs}
		return render(request, "job/index.html", context )



def JobDetailView(request, job_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		job = Job.objects.get(id=job_id)
		jobs = Job.objects.all()

		applied_status = False
		for item in job.applications.all():
			if item.app_user == app_user:
				applied_status = True


		context = {"app_user": app_user, "job": job, "jobs": jobs, "applied_status": applied_status}
		return render(request, "job/job_detail.html", context )



def ApplyJobView(request, job_id, app_user_id):
	app_user = AppUser.objects.get(id=app_user_id)
	job = Job.objects.get(id=job_id)

	application = Application.objects.create(app_user=app_user)
	application.save()

	ja = JobApplicationConnector(job=job, application=application)
	ja.save()

	messages.warning(request, "Job Applied!")
	return HttpResponseRedirect(reverse("job:index"))



	if request.method == "POST":
		pass


	else:
		job = Job.objects.get(id=job_id)
		jobs = Job.objects.all()

		context = {"app_user": app_user, "job": job, "jobs": jobs}
		return render(request, "job/apply_job.html", context )



def MyApplicationsView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)

	if request.method == "POST":
		pass


	else:
		my_applications = []
		jobs = Job.objects.all()

		for item in jobs:
			for jtem in item.applications.all():
				if jtem.app_user == app_user:
					my_applications.append(item)

		context = {"app_user": app_user, "my_applications": my_applications}
		return render(request, "job/my_applications.html", context )




def AddJobView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		title = request.POST.get("title")
		description = request.POST.get("description")

		job_type = request.POST.get("job_type")
		responsibility = request.POST.get("responsibility")
		requirement = request.POST.get("requirement")
		contact_email = request.POST.get("contact_email")
		contact_phone = request.POST.get("contact_phone")
		deadline = request.POST.get("deadline")

		job = Job.objects.create(app_user=app_user, title=title, description=description, job_type=job_type,
			responsibility=responsibility, requirement=requirement, contact_email=contact_email, contact_phone=contact_phone,
			deadline=deadline)
		job.save()

		messages.warning(request, "Job Added!")
		return HttpResponseRedirect(reverse("job:add_job"))


	else:
		jobs = Job.objects.filter(app_user=app_user)

		context = {"app_user": app_user, "jobs": jobs}
		return render(request, "job/add_job.html", context )





def JobApplicationsView(request, job_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		job = Job.objects.get(id=job_id)

		applications = job.applications.all()

		context = {"app_user": app_user, "job": job, "applications": applications}
		return render(request, "job/job_applications.html", context )





def EditJobView(request, job_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		job = Job.objects.get(id=job_id)

		title = request.POST.get("title")
		description = request.POST.get("description")

		job.title = title
		job.description = description
		job.save()

		messages.warning(request, "Job Edited!")
		return HttpResponseRedirect(reverse("job:add_job"))



	else:
		job = Job.objects.get(id=job_id)

		context = {"app_user": app_user, "job": job}
		return render(request, "job/edit_job.html", context )
