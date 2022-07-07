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

from quiz.models import *
from job.models import *

#from .forms import UserForm


def SetupQuizView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)

	if request.method == "POST":
		job_id = request.POST.get("job_id")
		job = Job.objects.get(id=job_id)

		title = request.POST.get("title")
		detail = request.POST.get("detail")
		duration = request.POST.get("duration")

		question_no = request.POST.get("question_no")
		barrier = request.POST.get("barrier")

		quiz = Quiz.objects.create(title=title, detail=detail, duration=duration,
			question_no=question_no, barrier=barrier)
		quiz.save()

		job.quiz = quiz
		job.save()

		return HttpResponseRedirect(reverse("quiz:add_qa", args=[quiz.id,]))


	else:
		my_jobs = Job.objects.filter(app_user=app_user)

		if my_jobs.count() == 0:
			messages.warning(request, "Add a job first")
			return HttpResponseRedirect(reverse("job:add_job"))

		else:
			context = {"app_user": app_user, "my_jobs": my_jobs}
			return render(request, "quiz/setup_quiz.html", context )


def AddQAView(request, quiz_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	quiz = Quiz.objects.get(id=quiz_id)
	if request.method == "POST":
		q1 = request.POST.get("q1")
		category = request.POST.get("category")
		level = request.POST.get("level")

		q1 = request.POST.get("q1")
		q2 = request.POST.get("q2")

		if q1 != "":
			q1_a = request.POST.get("q1_a")
			q1_b = request.POST.get("q1_b")
			q1_c = request.POST.get("q1_c")
			q1_d = request.POST.get("q1_d")
			answer_1 = request.POST.get("answer_1")

			question1 = QandA.objects.create(title=q1, answer_a=q1_a,
				answer_b=q1_b, answer_c=q1_c, answer_d=q1_d, answer=answer_1)
			question1.save()

			qq = QuizQandAConnector(quiz=quiz, qanda=question1)
			qq.save()


		if q2 != "":
			q2_a = request.POST.get("q2_a")
			q2_b = request.POST.get("q2_b")
			q2_c = request.POST.get("q2_c")
			q2_d = request.POST.get("q2_d")
			answer_2 = request.POST.get("answer_2")

			question2 = QandA.objects.create(title=q2, answer_a=q2_a,
				answer_b=q2_b, answer_c=q2_c, answer_d=q2_d, answer=answer_2)
			question2.save()

			qq = QuizQandAConnector(quiz=quiz, qanda=question2)
			qq.save()


		else:
			pass



		messages.warning(request, "Questions Successfully Added")
		return HttpResponseRedirect(reverse("job:index"))

		


	else:
		context = {"app_user": app_user, "quiz": quiz}
		return render(request, "quiz/add_qa.html", context )



def TakeQuizView(request, job_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)

	job = Job.objects.get(id=job_id)
	quiz = job.quiz

	questions = job.quiz.QandAs.all()

	counts = questions.count()
	count_list = []


	for i in range(counts):
		count_list.append(i+1)

	quiz_questions = zip(questions, count_list)

	if request.method == "POST":
		score = 0
		percentage = 0
		actual_score = 0
		real_score = 0

		answers = []
		answer_list = []
		for item, count in quiz_questions:
			val = "selected_answer_" + str(count)
			if request.POST.get(val):
				answers.append(request.POST.get(val))
			else:
				answers.append("x_x")

		for item in answers:
			answer_list.append(item.split("_")[1])


		for item, item2 in zip(questions, answer_list):
			if item.answer == item2:
				actual_score += 1

		percentage = (actual_score/counts)*100

		result = Result.objects.create(app_user=app_user, score=actual_score, total=count, percentage=percentage)
		result.save()

		jr = JobResultConnector(job=job, result=result)
		jr.save()

		return HttpResponseRedirect(reverse("quiz:complete_quiz", args=(result.id,)))


	else:

		context = {"app_user": app_user, "quiz": quiz, "quiz_questions": quiz_questions, "counts": counts}#, "time_exam_link": time_exam_link, "time_student_id": time_student_id}#, "time_result_id": time_result_id}
		return render(request, "quiz/take_quiz.html", context)



def CompleteQuizView(request, result_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	result = Result.objects.get(id=result_id)
	if request.method == "POST":
		pass


	else:

		context = {"result": result, "app_user": app_user}
		return render(request, "quiz/complete_quiz.html", context )



def SeeResultView(request, app_user_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	result = Result.objects.filter(app_user__id=app_user_id).last()
	if request.method == "POST":
		pass


	else:

		context = {"result": result, "app_user": app_user}
		return render(request, "quiz/see_result.html", context )





























