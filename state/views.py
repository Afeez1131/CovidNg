from django.shortcuts import render
from rest_framework import viewsets
from .models import Covid
from .serializer import StateSerializer
from django.http import HttpResponse

# Create your views here.


class StateListView(viewsets.ModelViewSet):
	queryset = Covid.objects.all()
	serializer_class = StateSerializer
	lookup_field = 'states_affected'
	http_method_names = ['get']


# class StateDeleteView(generics.RetrieveDestroyAPIView):
# 	queryset = Covid.objects.all()
# 	serializer_class = StateSerializer
