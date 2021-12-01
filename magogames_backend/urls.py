from django.urls import path

from . import views


urlpatterns = [
    path('externalAPI/home', views.get_homepageDeals),
    path('externalAPI/store', views.get_store),
    path('externalAPI/gameLookup/<int:id>', views.get_gameLookup),

]