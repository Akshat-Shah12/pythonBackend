
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',hello_world,name="hello"),
    path('add-student/',post_student,name="addStudent"),
    path('update-student/<id>/',update_student,name="updateStudent"),
    path('delete-student/<id>/',delete_student,name="deleteStudent"),
]
