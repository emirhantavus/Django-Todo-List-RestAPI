from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
      created_at = serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])      
      class Meta:
            model = Task
            fields = ['id','title','description','created_at','completed']