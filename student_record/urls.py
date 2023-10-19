from django.urls import path,include
from .views import *

urlpatterns = [
    path('',studenthomepage,name='stu_homepage'),
    path('show/',showstu,name='showstu'),
    path('create/',createstu,name="createstu"),
    path('edit/<int:rno>/',editstu,name='editstu'),
    path('delete/<int:rno>',deletestu,name='deletestu'),
]
