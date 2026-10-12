from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None,
}

def index(request):
    return HttpResponse(" this in main route of my first app")

def monthly_challenges_by_number(request,month):
    months=list(challenges.keys())
    if month >len(months):
        return HttpResponseNotFound("This month is not supported")
    try:
        month=months[month-1]
        redirect_path=reverse("month-challenge", kwargs={"month": month})
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")

def monthly_challenges(request,month):
    try:
        challenge_text=challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")