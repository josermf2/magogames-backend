from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
import requests


@api_view(['GET'])
def get_homepageDeals(request):    
    r = requests.get('https://www.cheapshark.com/api/1.0/deals?pageSize=40').json()   
    return Response(r) 
