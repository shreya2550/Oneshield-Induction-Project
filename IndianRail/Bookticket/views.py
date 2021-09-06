from django.shortcuts import render

# Create your views here.


# def home(request):
#   return render(request, 'index.html', {})


from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
def home(request):
    return render(request, 'index.html')


def booktick(request):
    return render(request, 'bookticket.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def myticket(request):
    return render(request, 'mytickets.html')


class BooktickView(TemplateView):
    template_name = "template/bookticket.html"


class Homeview(TemplateView):
    template_name = "template/index.html"


class Trainview(TemplateView):
    template_name = "template/train.html"


from datetime import date

today = date.today()


def booknow(request):
    return render(request, 'booknow.html')


def Time(request):
    return render(request, 'bookticket.html', {'today': today})


def train(request):
    return render(request, 'train.html')


def createpost(request):
    return render(request, 'bookticket.html')


def signup(request):
    return render(request, 'bookticket.html')
