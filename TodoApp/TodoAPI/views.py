from django.shortcuts import render , redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer


@api_view(['GET','POST'])
def todo(request):
      tasks = Task.objects.all()
      if request.method == 'GET':
            serialized_task = TaskSerializer(tasks,many=True)
            return render(request,'list.html',{'tasks':serialized_task.data})
      if request.method == 'POST':
            task = request.POST.get('title')
            desc = request.POST.get('description')
            Task.objects.create(title=task,description=desc)
            return redirect('list')