from django.shortcuts import render, redirect
from .models import Total
from .serializer import TotalActiveSerializer, TotalConfirmedSerializer,TotalDischargedSerializer, TotalDeathSerializer, TotalSampleSerializer, TotalSerializer
from rest_framework import viewsets
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
class TotalApi(viewsets.ModelViewSet):
	queryset = Total.objects.all()
	serializer_class = TotalConfirmedSerializer
	http_method_names = ['get']


class ActiveApi(viewsets.ModelViewSet):
	queryset = Total.objects.all()
	serializer_class = TotalActiveSerializer
	http_method_names = ['get']


class DischargedApi(viewsets.ModelViewSet):
	queryset = Total.objects.all()
	serializer_class = TotalDischargedSerializer
	http_method_names = ['get']


class DeathApi(viewsets.ModelViewSet):
	queryset = Total.objects.all()
	serializer_class = TotalDeathSerializer
	http_method_names = ['get']

class ConfirmedApi(viewsets.ModelViewSet):
	queryset = Total.objects.all()
	serializer_class = TotalConfirmedSerializer
	http_method_names = ['get']

class SampleApi(viewsets.ModelViewSet):
	queryset = Total.objects.all()
	serializer_class = TotalSampleSerializer
	http_method_names = ['get']


class TotalApi(viewsets.ModelViewSet):
	queryset = Total.objects.all()
	serializer_class = TotalSerializer
	http_method_names = ['get']

# class TotalDateApi(viewsets.ModelViewSet):
# 	queryset = TotalDate.objects.all()
# 	serializer_class = TotalDateSerializer
# 	lookup_field = 'date'


