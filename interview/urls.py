from django.urls import path
from . import views

app_name = "interview"

urlpatterns = [

	path("", views.IndexView, name="index"),
	
]