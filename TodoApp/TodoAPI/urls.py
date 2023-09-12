from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('todo/',views.todo),
    path('todo/<int:id>',views.singleTodo),
]