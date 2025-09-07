from django.shortcuts import render,HttpResponse

def home(req):
    return render(req, "core/index.html")

def redes_sociales(req):
    return render(req, "core/redes_sociales.html")

def faq(req):
    return render(req, "core/faq.html")