from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
# from .mypaginations import MyPageNumberPaginations
# from .mypaginations import MyLimitOffsetPaginations
from .mypaginations import MyCursorPaginations
# Create your views here.

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # pagination_class=MyPageNumberPaginations
    pagination_class=MyCursorPaginations