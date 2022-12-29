

from django.urls import path
from . import views

app_name = "staking"

urlpatterns = [

	path("stake/", views.StakeView, name="stake"),
	path("my-stakes/", views.MyStakesView, name="my_stakes"),

	path("make-payment/<int:staking_id>/", views.MakePaymentView, name="make_payment"),
	path("confirm-payment/<int:staking_id>/", views.ConfirmPaymentView, name="confirm_payment"),

	path("request-payment/<int:staking_id>/", views.RequestPaymentView, name="request_payment"),

]


