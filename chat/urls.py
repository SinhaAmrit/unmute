from django.urls import path
from chat import views

urlpatterns = [
    path("", views.index, name="index"),
    path("direct/<username>", views.Directs, name="directs"),
]
