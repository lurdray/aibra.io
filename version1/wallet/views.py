from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


from app_user.models import AppUser

# Create your views here.


def IndexView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		if app_user.wallet_address == "null":
			
			resp = requests.get("https://api.iotexchartapp.com/brise-create-wallet/").json()
			wallet_address = resp["wallet_address"]
			wallet_key = resp["wallet_key"]

			app_user.wallet_address = wallet_address
			app_user.wallet_key = wallet_key
			app_user.save()


		resp = requests.get("https://api.iotexchartapp.com/brise-get-balance/%s" % (app_user.wallet_address)).json()
		data = resp["data"]

		brise_balance = data[0]["balance"]

		total = 0

		for item in data:
			total += float(item['total_price'])


		context = {"app_user": app_user, "brise_balance": brise_balance, "total": total, "data": data}
		return render(request, "wallet/index.html", context )




def UpdateProfileView(request):
	if request.method == "POST":
		first_name = request.POST.get("first_name")
		last_name = request.POST.get("last_name")
		age = request.POST.get("age")
		address = request.POST.get("address")
		country = request.POST.get("country")

		app_user = AppUser.objects.get(user__pk=request.user.id)

		if first_name != "":
			app_user.first_name = first_name

		if last_name != "":
			app_user.last_name = last_name

		if age != "":
			app_user.age = age
			app_user.address = address
			app_user.country = country
			app_user.save()

		messages.warning(request, "Profile updated successfully!")
		return HttpResponseRedirect(reverse("wallet:update_profile"))



	else:
		app_user = AppUser.objects.get(user__pk=request.user.id)

		context = {"app_user": app_user}
		return render(request, "wallet/update_profile.html", context )

def SendView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
	    pass
	    
	else:
		
		context = {"app_user": app_user}
		return render(request, "wallet/send.html", context)

def SendTokenView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
	    pass

	else:
		
		context = {"app_user": app_user}
		return render(request, "wallet/send_token.html", context)


def BriseNameView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		context = {"app_user": app_user}
		return render(request, "wallet/bns.html", context )



