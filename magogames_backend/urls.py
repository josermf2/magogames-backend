from django.urls import path

from knox import views as knox_views
from . import views


urlpatterns = [
    path('externalAPI/home', views.get_homepageDeals),
    path('externalAPI/store', views.get_store),
    path('externalAPI/gameLookup/<int:id>', views.get_gameLookup),
    path('externalAPI/dealLookup/<slug:deal>', views.get_dealLookup),
    path('externalAPI/search/<str:title>', views.get_search),
    path('externalAPI/search/min/<str:title>/<int:minprice>', views.get_search),
    path('externalAPI/search/max/<str:title>/<int:maxprice>', views.get_search),
    path('externalAPI/search/min/<int:minprice>', views.get_search),
    path('externalAPI/search/max/<int:maxprice>', views.get_search),
    path('externalAPI/search/<int:minprice>/<int:maxprice>', views.get_search),
    path('externalAPI/search/<str:title>/<int:minprice>/<int:maxprice>', views.get_search),
    path('API/register/', views.RegisterAPI.as_view()),
    path('API/login/', views.LoginAPI.as_view(), name='login'),
    path('API/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('API/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('API/favorite/<str:user_name>/', views.api_get_favorite),
    path('API/favorite', views.api_post_favorite),    
    path('API/favorite/delete', views.api_delete_favorite),    
]