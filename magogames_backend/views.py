from django.shortcuts import render, redirect
from django.contrib.auth import login
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .serializers import UserSerializer, RegisterSerializer, FavoriteSerializer
from django.http import Http404
from .models import User, Favorite
import requests

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        newUser = User()
        newUser.name = request.data['username']
        newUser.save()
        
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

@api_view(['GET'])
def get_homepageDeals(request):    
    r = requests.get('https://www.cheapshark.com/api/1.0/deals?pageSize=40').json()   
    return Response(r) 

@api_view(['GET'])
def get_store(request):    
    r = requests.get('https://www.cheapshark.com/api/1.0/stores').json()   
    return Response(r) 

@api_view(['GET'])
def get_gameLookup(request, id):    
    r = requests.get('https://www.cheapshark.com/api/1.0/games?id='+str(id)).json()   
    return Response(r) 

@api_view(['GET'])
def get_dealLookup(request, deal):    
    r = requests.get('https://www.cheapshark.com/api/1.0/deals?id='+str(deal)).json()   
    return Response(r) 

@api_view(['GET'])
def get_search(request, title='', minprice='', maxprice=''):
    if title != '':
        if minprice != '' and maxprice != '':
            r = requests.get('https://www.cheapshark.com/api/1.0/deals?title='+str(title)+'&lowerPrice='+str(minprice)+'&upperPrice='+str(maxprice)).json()
            return Response(r)
        elif minprice != '':
            r = requests.get('https://www.cheapshark.com/api/1.0/deals?title='+str(title)+'&lowerPrice='+str(minprice)).json()
            return Response(r)
        elif maxprice != '':
            r = requests.get('https://www.cheapshark.com/api/1.0/deals?title='+str(title)+'&upperPrice='+str(maxprice)).json()
            return Response(r) 
        else:
            r = requests.get('https://www.cheapshark.com/api/1.0/deals?title='+str(title)).json()
            return Response(r)
    else:
        if minprice != '' and maxprice != '':
            r = requests.get('https://www.cheapshark.com/api/1.0/deals?&lowerPrice='+str(minprice)+'&upperPrice='+str(maxprice)).json()
            return Response(r)
        elif minprice != '':
            r = requests.get('https://www.cheapshark.com/api/1.0/deals?lowerPrice='+str(minprice)).json()
            return Response(r)
        elif maxprice!= '':
            r = requests.get('https://www.cheapshark.com/api/1.0/deals?upperPrice='+str(maxprice)).json()
            return Response(r)

@api_view(['GET'])
def api_get_favorite(request, user_name):                
    try:
        favorites = Favorite.objects.filter(user=User.objects.get(name=user_name))
    except User.DoesNotExist:
        raise Http404()

    serialized_favorites = FavoriteSerializer(favorites, many=True)
    return Response(serialized_favorites.data)

@api_view(['POST'])
def api_post_favorite(request):                
    if request.method == 'POST':
        favorite = Favorite()
        favorite_data = request.data
        favorite.user = User.objects.get(name=favorite_data['user'])
        favorite.favorite = favorite_data['favorite']
        favorite.save()

    serialized_favorite = FavoriteSerializer(favorite)
    return Response(serialized_favorite.data)

@api_view(['DELETE'])
def api_delete_favorite(request):                
    favorite = Favorite.objects.get(user=User.objects.get(name=request.data['user']), favorite=request.data['favorite'])
    favorite.delete()

    serialized_favorite = FavoriteSerializer(favorite)
    return Response(serialized_favorite.data)

