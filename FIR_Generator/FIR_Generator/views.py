from django.shortcuts import render, redirect, HttpResponse,get_object_or_404


def landingPage(request):
    return render(request, "main/landing.html")