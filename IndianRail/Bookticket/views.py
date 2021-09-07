# Create your views here.
from django.shortcuts import render
from datetime import date
from django.contrib.auth.hashers import make_password, check_password
from .models import Customer
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.db import connection
from django.views.generic.base import TemplateView

# def home(request):
#   return render(request, 'index.html', {})


# Create your views here.
def home(request):
    return render(request, 'index.html')


def booktick(request):
    return render(request, 'bookticket.html')


def login(request):
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('password'):
            email = request.POST.get('email')
            password = request.POST.get('password')
            extracted_email = []
            x = Customer.objects.get(Email=email)
            extracted_email.append(x)
            sql = 'select "Password" from "Bookticket_customer"'
            cursor = connection.cursor()
            raw_data = []
            cursor.execute(sql, ['localhost'])
            row = cursor.fetchall()
            for r in row:
                raw_data.append(r)
            cleaned_password = ""
            #print(raw_data)
            list_cleaned_password = []
            for i in raw_data:
                for h in i:
                    if h == '(':
                        pass
                        #print("hello")
                    else:
                        cleaned_password = cleaned_password + h
                list_cleaned_password.append(cleaned_password)
                cleaned_password = ""
            for q in list_cleaned_password:
                if Customer.objects.filter(Email=email, Password=q):
                    flag = 1
                else:
                    flag = 0
                if flag == 1:
                    print("User exists in the Database.")
                    print("User search Successfull .")
                x = check_password(password, q)
                if x == True:
                    print("Login Successfull.")
                    return render(request, 'index.html')
            print("Login Unsuccessfull")
            return render(request, 'login.html')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    '''if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        conn = psycopg2.connect(
            database="mydb", user='postgres', password='shreya1project', host='127.0.0.1', port='5432'
        )
        # Setting auto commit false
        conn.autocommit = True
        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        #first_person = Customer.objects.raw('SELECT * FROM "Bookticket_customer" ')[0]
        name=''
        for p in Customer.objects.raw('SELECT * FROM "Bookticket_customer" WHERE '):
            print(p.Email, p.Name)
        #print(first_person)

        print(email)
        print(password)
    return render(request, 'login.html')'''


def register(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('age') and request.POST.get(
                'phone') and request.POST.get('password'):
            post = Customer()
            post.Name = request.POST.get('name')
            post.Email = request.POST.get('email')
            post.Age = request.POST.get('age')
            post.Phone = request.POST.get('phone')
            post.Password = make_password(request.POST.get('password'))
            post.save()
            return redirect('/login')
        else:
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def myticket(request):
    return render(request, 'mytickets.html')


class BooktickView(TemplateView):
    template_name = "template/bookticket.html"


class Homeview(TemplateView):
    template_name = "template/index.html"


class Trainview(TemplateView):
    template_name = "template/train.html"


def booknow(request):
    return render(request, 'booknow.html')


def time(request):
    today = date.today()
    return render(request, 'bookticket.html', {'today': today})


def train(request):
    return render(request, 'train.html')


def createpost(request):
    return render(request, 'bookticket.html')


def signup(request):
    return render(request, 'bookticket.html')
