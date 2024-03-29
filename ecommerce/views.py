from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Catageory, Products
# Create your views here.


def home(request):

    return render(request, 'home.html')


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username, email=email, password=password)

        user.save()

    return render(request, 'register.html')

def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:

            login(request, user)

            return redirect('products')
        else:
            print("invalid details")
            return redirect('login.html')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)

    return redirect('home')


def products(request):

    catageory = request.GET.get('catageory')

    if catageory == None:
        products = Products.objects.all()
    else:
        products = Products.objects.filter(catageory__name = catageory)

    catageories = Catageory.objects.all()

    context = {
        'catageories':catageories,
        'products':products,
    }

    return render(request, "products.html", context)



def to_cart(request, pk):

    products = Products.objects.get(id=pk)

    return render(request, "cart.html", {"products":products})


def orders(request):

    return render(request, 'orders.html')


def payments(request):

    return render(request, 'payment.html')


def profile_data(request):

    return render(request, "profile.html")

