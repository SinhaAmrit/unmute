from django.urls import path
from chat import views

urlpatterns = [
    path("", views.index, name="index"),
    path("directs/<username>", views.Directs, name="directs"),
]
