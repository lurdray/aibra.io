from django.urls import path
from . import views

app_name = "wallet"

urlpatterns = [

	path("", views.IndexView, name="index"),
	path("update/profile/", views.UpdateProfileView, name="update_profile"),

]