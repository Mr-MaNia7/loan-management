from django.shortcuts import render


def showHomeView(request):
    return render(request, "index.html")
