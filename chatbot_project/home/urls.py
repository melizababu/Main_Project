
from django.urls import path,include
from . import views

urlpatterns= [
  path('',views.index,name='index'),
  #path('get-semester/', views.get_semester, name='get_semester'),
 # path('get-answer/', views.get_answer, name='get_answer'),
  path('query_bus/', views.query_bus_details, name='query_bus_details'),



]
