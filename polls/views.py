from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Question


# Create your views here.
def index(request):
    latest_question_list: [list] = Question.objects.order_by("pub_date")[:5]
    # context is a dict() that holds the python variables which is sent to the template
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, template_name="polls/index.html", context=context)


def get_question_details(request, question_id):
    return HttpResponse(f"You're viewing question {question_id}")


def get_question_results(request, question_id):
    return HttpResponse(f"You're viewing results of question {question_id}")


def vote_question(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
