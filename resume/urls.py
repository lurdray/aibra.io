from django.urls import path
from . import views

app_name = "resume"

urlpatterns = [

	path("", views.IndexView, name="index"),
	path("update/resume/1/", views.UpdateResume1View, name="update_resume1"),

	path("update/resume/2/", views.UpdateResume2View, name="update_resume2"),

	path("update/resume/3/", views.UpdateResume3View, name="update_resume3"),
	path("update/resume/3/add-career/", views.AddCareerView, name="add_career"),
	path("update/resume/3/add-education/", views.AddEducationView, name="add_education"),
	path("update/resume/3/add-skill/", views.AddSkillView, name="add_skill"),

	path("update/resume/4/", views.UpdateResume4View, name="update_resume4"),
	path("update/resume/4/add-project/", views.AddProjectView, name="add_project"),
	path("update/resume/4/add-hobby/", views.AddHobbyView, name="add_hobby"),

	path("update/resume/5/", views.UpdateResume5View, name="update_resume5"),
	path("update/resume/5/add-award/", views.AddAwardView, name="add_award"),
	path("update/resume/5/add-referee/", views.AddRefereeView, name="add_referee"),


]