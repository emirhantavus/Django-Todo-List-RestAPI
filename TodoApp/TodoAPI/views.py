from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer


@api_view(['GET','POST'])
def todo(request):
      if request.method == 'GET':
            tasks = Task.objects.all()
            serialized_task = TaskSerializer(tasks,many=True)
            return Response(serialized_task.data,status.HTTP_200_OK)
      if request.method == 'POST':
            serialized_task = TaskSerializer(data = request.data)
            serialized_task.is_valid(raise_exception=True)
            serialized_task.save()
            return Response(serialized_task.data , status.HTTP_201_CREATED)


@api_view(['GET','DELETE','PUT'])
def singleTodo(request,id):
      if request.method == 'GET':
            task = Task.objects.get(pk=id)
            serialized_task = TaskSerializer(task)
            return Response(serialized_task.data,status.HTTP_200_OK)

      elif request.method == 'DELETE':
            task = Task.objects.get(pk=id)
            task.delete()
            message = {'message':'object is deleted'} 
            return Response(message,status.HTTP_200_OK)
      elif request.method == 'PUT':
            tasks = Task.objects.get(pk=id)
            serialized_task = TaskSerializer(tasks,data = request.data)
            if serialized_task.is_valid():
                  serialized_task.save()
                  message = {'message':'object is updated'}
                  return Response(message,status.HTTP_200_OK)