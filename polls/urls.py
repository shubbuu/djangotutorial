from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"), # we havn't created template for vote








    # # eg: /polls/
    # path("", views.index, name="index"),

    # # eg: /polls/5/ 
    # path("<int:question_id>/", views.detail, name="detail"),

    # # eg: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),

    # # eg: 
    # path("<int:question_id>/vote/", views.vote, name="vote")
]