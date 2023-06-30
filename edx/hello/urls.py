from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("soumya/",views.soumya,name="soumya"),
    path("<str:name>",views.greet,name="greet")
]