from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # /polls/
    path("", views.index, name="index"),
    # /polls/5/
    path("<int:question_id>/", views.get_question_details, name="question_details"),
    # /polls/5/results/
    path("<int:question_id>/results/", views.get_question_results, name="question_results"),
    # /polls/5/vote/
    path("<int:question_id>/vote/", views.vote_question, name="vote_question"),
]
