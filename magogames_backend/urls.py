from django.urls import path

from . import views


urlpatterns = [
    path('externalAPI/home', views.get_homepageDeals),
    path('externalAPI/store', views.get_store),
    path('externalAPI/gameLookup/<int:id>', views.get_gameLookup),
    path('externalAPI/search/<str:title>', views.get_search),
    path('externalAPI/search/min/<str:title>/<int:minprice>', views.get_search),
    path('externalAPI/search/max/<str:title>/<int:maxprice>', views.get_search),
    path('externalAPI/search/min/<int:minprice>', views.get_search),
    path('externalAPI/search/max/<int:maxprice>', views.get_search),
    path('externalAPI/search/<int:minprice>/<int:maxprice>', views.get_search),
    path('externalAPI/search/<str:title>/<int:minprice>/<int:maxprice>', views.get_search),
]