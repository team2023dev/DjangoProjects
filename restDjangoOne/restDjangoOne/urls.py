"""restDjangoOne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from api import views
# from api1 import views
# from api4 import views
from api22 import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
# from api16.auth import CustomAuthToken 
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router=DefaultRouter()

# router.register('studentapi',views.StudentModelViewSet,basename='student')
router.register('singer',views.SingerViewSet,basename='singer')
router.register('song',views.SongViewSet,basename='song')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("studentapi/",views.StudentList.as_view()),
    # path("studentapi/<int:pk>/",views.student_api)
    path("", include(router.urls)),
    # path("gettoken/",TokenObtainPairView.as_view(),name='token_obtain_pair'),
    # path("refreshtoken/",TokenRefreshView.as_view(),name='token_refresh'),
    # path("verifytoken/",TokenVerifyView.as_view(),name='token_verify'),
    path("auth/",include('rest_framework.urls',namespace='rest_framework')),
    # path('gettoken/',CustomAuthToken.as_view())
    # path("studentapi/<int:pk>/",views.StudentRetrieve.as_view()),
    # path("studentapi/",views.StudentListCreate.as_view()),
    # path("studentapi/<int:pk>/",views.StudentUpdateRetrieve.as_view()),
    # path("studentapi/<int:pk>/",views.StudentRetrieveDelete.as_view()),
    # path("studentapi/<int:pk>/",views.StudentUpdateRetrieveDelete.as_view()),
    # path("studentapi/<int:pk>/",views.StudentUpdate.as_view()),
    # path("studentapi/<int:pk>/",views.StudentDelete.as_view()),
    # path("studentapi/",views.StudentList.as_view()),
    # path("studentapi/",views.StudentCreate.as_view()),
    # path("studentapi/",views.LCStudent.as_view()),
    # path("studentapi/<int:pk>/",views.RUDStudent.as_view())
    # path("studentapi/",views.StudentCreate.as_view()),
    # path("stuinfo/<int:pk>",viewsapi.student_detail),
    # path("stuinfo/",viewsapi.student_list),
    # path("stucreate/",views.student_create)
    # path("studentapi/",views.StudentList.as_view()),
    # path("studentapi/<int:pk>/",views.StudentRetrieve.as_view()),
    # path("studentapi/<int:pk>/",views.StudentUpdate.as_view()),
    # path("studentapi/<int:pk>/",views.StudentDelete.as_view())
]