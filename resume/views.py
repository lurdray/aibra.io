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

from app_user.models import AppUser
from resume.models import *



def IndexView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		context = {"app_user": app_user}
		return render(request, "resume/index.html", context )





def UpdateResume1View(request):
	if request.method == "POST":
		app_user = AppUser.objects.get(user__pk=request.user.id)

		title = request.POST.get("title")
		opening_statement = request.POST.get("opening_statement")

		title = Title.objects.create(title=title, status=True)
		title.save()

		opening_statement = OpeningStatement.objects.create(opening_statement=opening_statement, status=True)
		opening_statement.save()


		rt = ResumeTitleConnector(resume=app_user.resume, title=title)
		rt.save()
		ro = ResumeOpeningStatementConnector(resume=app_user.resume, opening_statement=opening_statement)
		ro.save()

		
		if app_user.resume.resume_status == False:
			app_user.resume.resume_status = True
			app_user.resume.resume_cent = 20
			app_user.save()
			
		messages.warning(request, "Welldone! Resume Updated successfully!")
		return HttpResponseRedirect(reverse("resume:update_resume2"))


	else:
		app_user = AppUser.objects.get(user__pk=request.user.id)

		context = {"app_user": app_user, "title": app_user.resume.titles.first(), "opening_statement": app_user.resume.opening_statements.first()}
		return render(request, "resume/update_resume1.html", context )




def UpdateResume2View(request):
	if request.method == "POST":
		app_user = AppUser.objects.get(user__pk=request.user.id)

		work_experience = request.POST.get("work_experience")
		date_from = request.POST.get("date_from")
		date_to = request.POST.get("date_to")

		work_experience = WorkExperience.objects.create(work_experience=work_experience, date_from=date_from, date_to=date_to, status=True)
		work_experience.save()

		rw = ResumeWorkExperienceConnector(resume=app_user.resume, work_experience=work_experience)
		rw.save()

		if app_user.resume.work_experience_status == False:
			app_user.resume.work_experience_status = True
			app_user.resume.resume_cent = 40
			app_user.save()
			
		messages.warning(request, "Welldone! Resume Updated successfully!")
		return HttpResponseRedirect(reverse("resume:update_resume2"))



	else:
		app_user = AppUser.objects.get(user__pk=request.user.id)

		context = {"app_user": app_user, "work_experiences": app_user.resume.work_experiences}
		return render(request, "resume/update_resume2.html", context )



def UpdateResume3View(request):
	if request.method == "POST":
		pass


	else:
		app_user = AppUser.objects.get(user__pk=request.user.id)

		context = {"app_user": app_user, "careers": app_user.resume.careers,
		"educations": app_user.resume.educations, "skills": app_user.resume.skills}
		return render(request, "resume/update_resume3.html", context )



def AddCareerView(request):

	if request.method == "POST":
		app_user = AppUser.objects.get(user__pk=request.user.id)

		career = request.POST.get("career")
		date_from = request.POST.get("date_from")
		date_to = request.POST.get("date_to")

		career = Career.objects.create(career=career, date_from=date_from, date_to=date_to, status=True)
		career.save()

		rc = ResumeCareerConnector(resume=app_user.resume, career=career)
		rc.save()

			
		messages.warning(request, "Welldone! Resume Updated successfully!")
		return HttpResponseRedirect(reverse("resume:update_resume3"))



	else:
		app_user = AppUser.objects.get(user__pk=request.user.id)

		context = {"app_user": app_user}
		return render(request, "resume/add_career.html", context )



def AddEducationView(request):

	if request.method == "POST":
		app_user = AppUser.objects.get(user__pk=request.user.id)

		education = request.POST.get("education")
		date_from = request.POST.get("date_from")
		date_to = request.POST.get("date_to")

		education = Education.objects.create(education=education, date_from=date_from, date_to=date_to, status=True)
		education.save()

		rc = ResumeEducationConnector(resume=app_user.resume, education=education)
		rc.save()

			
		messages.warning(request, "Welldone! Resume Updated successfully!")
		return HttpResponseRedirect(reverse("resume:update_resume3"))



	else:
		app_user = AppUser.objects.get(user__pk=request.user.id)

		context = {"app_user": app_user}
		return render(request, "resume/add_education.html", context )


def AddSkillView(request):

	if request.method == "POST":
		app_user = AppUser.objects.get(user__pk=request.user.id)

		skill = request.POST.get("skill")
		date_from = request.POST.get("date_from")
		date_to = request.POST.get("date_to")

		skill = Skill.objects.create(skill=skill, date_from=date_from, date_to=date_to, status=True)
		skill.save()

		rs = ResumeSkillConnector(resume=app_user.resume, skill=skill)
		rs.save()

		messages.warning(request, "Welldone! Resume Updated successfully!")
		return HttpResponseRedirect(reverse("resume:update_resume3"))



	else:
		app_user = AppUser.objects.get(user__pk=request.user.id)

		context = {"app_user": app_user}
		return render(request, "resume/add_skill.html", context )




def AddProjectView(request):

	if request.method == "POST":
		app_user = AppUser.objects.get(user__pk=request.user.id)

		project = request.POST.get("project")
		detail = request.POST.get("detail")
		link = request.POST.get("link")

		project = Project.objects.create(project=project, detail=detail, link=link, status=True)
		project.save()

		rp = ResumeProjectConnector(resume=app_user.resume, project=project)
		rp.save()

		messages.warning(request, "Welldone! Resume Updated successfully!")
		return HttpResponseRedirect(reverse("resume:update_resume3"))



	else:
		app_user = AppUser.objects.get(user__pk=request.user.id)

		context = {"app_user": app_user}
		return render(request, "resume/add_project.html", context )



def AddHobbyView(request):

	if request.method == "POST":
		app_user = AppUser.objects.get(user__pk=request.user.id)

		hobby = request.POST.get("hobby")

		hobby = Hobby.objects.create(hobby=hobby, status=True)
		hobby.save()

		rh = ResumeHobbyConnector(resume=app_user.resume, hobby=hobby)
		rh.save()

		messages.warning(request, "Welldone! Resume Updated successfully!")
		return HttpResponseRedirect(reverse("resume:update_resume3"))



	else:
		app_user = AppUser.objects.get(user__pk=request.user.id)

		context = {"app_user": app_user}
		return render(request, "resume/add_hobby.html", context )





def AddAwardView(request):

	if request.method == "POST":
		app_user = AppUser.objects.get(user__pk=request.user.id)

		award = request.POST.get("award")
		detail = request.POST.get("detail")
		year = request.POST.get("year")
		link = request.POST.get("link")

		award = Award.objects.create(award=award, detail=detail, year=year, link=link, status=True)
		award.save()

		ra = ResumeAwardConnector(resume=app_user.resume, award=award)
		ra.save()

		messages.warning(request, "Welldone! Resume Updated successfully!")
		return HttpResponseRedirect(reverse("resume:update_resume3"))



	else:
		app_user = AppUser.objects.get(user__pk=request.user.id)

		context = {"app_user": app_user}
		return render(request, "resume/add_award.html", context )




def AddRefereeView(request):

	if request.method == "POST":
		app_user = AppUser.objects.get(user__pk=request.user.id)

		referee = request.POST.get("referee")
		phone_no = request.POST.get("phone_no")
		place_of_work = request.POST.get("place_of_work")

		referee = Referee.objects.create(referee=referee, phone_no=phone_no, place_of_work=place_of_work, status=True)
		referee.save()

		rr = ResumeAwardConnector(resume=app_user.resume, referee=referee)
		rr.save()

		messages.warning(request, "Welldone! Resume Updated successfully!")
		return HttpResponseRedirect(reverse("resume:update_resume3"))



	else:
		app_user = AppUser.objects.get(user__pk=request.user.id)

		context = {"app_user": app_user}
		return render(request, "resume/add_referee.html", context )



def UpdateResume4View(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "resume/update_resume4.html", context )



def UpdateResume5View(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "wallet/update_resume5.html", context )

