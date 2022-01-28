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

from .forms import UserForm
from .models import AppUser
from resume.models import Resume

import random
import string

def ray_randomiser(length=6):
	landd = string.ascii_letters + string.digits
	return ''.join((random.choice(landd) for i in range(length)))


def SignInView(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)

				app_user = AppUser.objects.get(user__pk=request.user.id)

				print("11111111111111111111111111111111")
				messages.success(request, "Welcome Onboard")
				return HttpResponseRedirect(reverse("app_user:app"))
			else:
				print("22222222222222222222222222222222")
				messages.warning(request, "Sorry, Invalid Login Details")
				return HttpResponseRedirect(reverse("app_user:sign_in"))

		else:
			print("33333333333333333333333333333333333333")
			messages.warning(request, "Sorry, Invalid Login Details")
			return HttpResponseRedirect(reverse("app_user:sign_in"))

	else:
		context = {}
		return render(request, "app_user/sign_in.html", context )




def SignUpView(request):
	if request.method == "POST":

		form = UserForm(request.POST or None, request.FILES or None)
		email = request.POST.get("username")
		first_name = request.POST.get("first_name")
		last_name = request.POST.get("last_name")
		account_type = request.POST.get("account_type")


		if request.POST.get("password2") != request.POST.get("password1"):
			messages.warning(request, "Make sure both passwords match")
			return HttpResponseRedirect(reverse("app_user:sign_up"))

			
		else:
			try:
				AppUser.objects.get(user__email=request.POST.get("username"))
				messages.warning(request, "Email Address already taken, try another one!")
				return HttpResponseRedirect(reverse("app_user:sign_up"))


			except:
				user = form.save()
				user.set_password(request.POST.get("password1"))
				user.save()

				app_user = AppUser.objects.create(user=user, account_type=account_type)
				app_user.otp_code = ray_randomiser()

				resume = Resume.objects.create()
				resume.save

				app_user.resume = resume
				app_user.save()

				user = app_user.user
				user.email = email
				user.save()

				if user:
					if user.is_active:
						login(request, user)

						app_user = AppUser.objects.get(user__pk=request.user.id)
						messages.warning(request, "Authenticate your account, your otp code has been sent to your email.")
						return HttpResponseRedirect(reverse("app_user:complete_sign_up"))

	else:
		form = UserForm()
		context = {"form": form}
		return render(request, "app_user/sign_up.html", context )



	return render(request, "app_user/sign_up.html", context )


def CompleteSignUpView(request):
	if request.method == "POST":
		otp = request.POST.get("otp")
		
		app_user = AppUser.objects.get(user__pk=request.user.id)
		if otp == app_user.otp_code:
			app_user.ec_status = True
			app_user.save()

			messages.warning(request, "Welcome Onboard!")
			return HttpResponseRedirect(reverse("app_user:app"))

		else:
			messages.warning(request, "Sorry, Invalid OTP Code.")
			return HttpResponseRedirect(reverse("app_user:complete_sign_up"))


	else:
		context = {}
		return render(request, "app_user/complete_sign_up.html", context )





def SignOutView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "app_user/sign_out.html", context )



def AppView(request):
	if request.method == "POST":
		pass


	else:
		app_user = AppUser.objects.get(user__pk=request.user.id)

		context = {"app_user": app_user}
		return render(request, "app_user/app2.html", context )



def AllRecruitView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		recruits = AppUser.objects.filter(account_type="candidate").order_by('-pub_date')

		context = {"recruits": recruits}
		return render(request, "app_user/all_recruits.html", context )



def AppUserDetailView(request, app_user_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		recruit = AppUser.objects.get(id=app_user_id)

		context = {"app_user": app_user, "recruit": recruit}
		return render(request, "app_user/app_user_detail.html", context )


def TempView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "app_user/app.html", context )



def ProfileView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "app_user/profile.html", context )

