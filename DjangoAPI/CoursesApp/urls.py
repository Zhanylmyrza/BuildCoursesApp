from django.urls import  path
from CoursesApp import views
from CoursesApp.views import courseApi
from CoursesApp.views import courseDetailView

urlpatterns = [
    path("course", views.courseApi.as_view()),
    path("course/<int:id>",courseDetailView.as_view()),
]

