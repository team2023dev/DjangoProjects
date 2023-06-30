from django.shortcuts import render
from django.http import HttpResponse
from .serializers import StudentSerializer
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_create(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Created'}
            jsondata=JSONRenderer().render(res)
            return HttpResponse(jsondata,content_type='application/json')
        jsondata=JSONRenderer().render(serializer.errors)
        return HttpResponse(jsondata,content_type='application/json')