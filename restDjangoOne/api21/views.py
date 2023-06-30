from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
# Create your views here.

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[OrderingFilter]
    ordering_fields=['name']
    # def get_queryset(self):
    #     user=self.request.user
    #     return Student.objects.filter(passby=user)
    # filter_backends=[DjangoFilterBackend]
    # filter_backends=[SearchFilter]
    # filterset_fields=['name','^city']