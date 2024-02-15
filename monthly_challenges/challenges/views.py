from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


list1={"january":"Join gym",
      "february":"Do cardio",
      "march":"Study",
      "april":"Run every day",
      "may":"Swim",
      "june":"train your dog",
      "july":"get a job",
      "auguest":"do steroids",
      "september":"bench 100kg",
      "octuber":"learn to drive",
      "november":"get a new car",
      "december":"go on holiday"}

def index(request):
 list_item=""
 months=list(list1.keys())
 for month in months:
  url=reverse("monthly_challenges",args=[month])
  list_item+=f"<li><a href=\"{url}\">{month}</a></li>" 
 respose=f"<ul>{list_item}</ul>"
 return HttpResponse(respose)
 
 

def monthly_challenges_withnumber(request,month):
  months=list(list1.keys())

  if month>len(months):return HttpResponseNotFound("Number excede available rage")

  redirct=months[month-1]
  redirct_url=reverse("monthly_challenges",args=[redirct])
  return HttpResponseRedirect(redirct_url)

def monthly_challenges(request,month):
  try :
    txt=list1[month]
    return render(request,"challenges/challenge.html",{
    'text':txt , 'month':month
    })
  except:
    return HttpResponseNotFound("Month name is incorrect")
  
  
  
    
