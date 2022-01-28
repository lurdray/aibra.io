from django.urls import path
from . import views

app_name = "job"

urlpatterns = [

	path("", views.IndexView, name="index"),
	path("job-detail/<int:job_id>/", views.JobDetailView, name="job_detail"),
	path("apply-job/<int:job_id>/<int:app_user_id>/", views.ApplyJobView, name="apply_job"),
	path("my-applications/", views.MyApplicationsView, name="my_applications"),

	path("add-job/", views.AddJobView, name="add_job"),
	path("job-applications<int:job_id>/", views.JobApplicationsView, name="job_applications"),
	path("edit-job/<int:job_id>/", views.EditJobView, name="edit_job"),
	
]