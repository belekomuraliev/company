import json
from django.http import HttpResponse
from .models import Cody, Employee
from .serializers import CodySerializer, EmployeeSerializer
from rest_framework import generics
from rest_framework import viewsets


class CodyViewCreate(generics.ListCreateAPIView):
    queryset = Cody.objects.all()
    serializer_class = CodySerializer

class EmployeeViewCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer





def get_cody_title(request):
    titles = Cody.objects.all()
    data = []
    for title in titles:
        list = {'title':title.title, 'department':title.department}
        data.append(list)
    return HttpResponse(json.dumps(data))


