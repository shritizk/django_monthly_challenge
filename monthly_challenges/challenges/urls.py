from django.urls import path
from . import views

urlpatterns=[
  path("<int:month>",views.monthly_challenges_withnumber),
  path("<str:month>",views.monthly_challenges,name="monthly_challenges")
  ,path("",views.index)
] 

