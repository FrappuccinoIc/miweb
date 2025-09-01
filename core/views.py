from django.shortcuts import render,HttpResponse

def home(req):
    return render(req, "core/index.html")

def foro(req):
    return render(req, "core/foro.html")

def faq(req):
    return render(req, "core/faq.html")