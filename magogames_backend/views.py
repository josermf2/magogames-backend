from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
import requests


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
