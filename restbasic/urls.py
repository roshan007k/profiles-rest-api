from django.urls import path
from restbasic import views

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
]
