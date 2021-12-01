from django.urls import path

from . import views


urlpatterns = [
    path('externalAPI/home', views.get_homepageDeals),
]