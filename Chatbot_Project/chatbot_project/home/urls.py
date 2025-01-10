
from django.urls import path,include
from . import views

urlpatterns= [
  path('',views.index,name='index'),
  path('get-semester/', views.get_semester, name='get_semester'),
]
