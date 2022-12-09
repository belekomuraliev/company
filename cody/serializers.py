from rest_framework import serializers
from .models import Cody, Employee



class CodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cody
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'