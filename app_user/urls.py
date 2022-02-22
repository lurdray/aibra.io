from django.urls import path
from . import views

app_name = "app_user"

urlpatterns = [


	path("sign-in/", views.SignInView, name="sign_in"),
	path("sign-up/", views.SignUpView, name="sign_up"),
	path("maintain/", views.MaintainView, name="maintain"),
	path("sign-up/complete/", views.CompleteSignUpView, name="complete_sign_up"),
	path("sign-out/", views.SignOutView, name="sign_out"),

	path("", views.AppView, name="app"),
	path("app/update-profile/", views.UpdateAppuserView, name="update_appuser"),
	path("recruits/", views.AllRecruitView, name="all_recruits"),
	path("app-user-detail/<int:app_user_id>/", views.AppUserDetailView, name="app_user_detail"),

	path("temp/", views.TempView, name="temp"),

]