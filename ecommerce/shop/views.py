from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from shop.models import Category,Product
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def allcategories(request):
    k=Category.objects.all()
    return render(request,'category.html',{'c':k})


def allproducts(request,p):
    c=Category.objects.get(name=p)
    p=Product.objects.filter(category=c)
    return render(request,'product.html',{'c':c,'p':p})

def details(request, p):
    p = Product.objects.get( name=p)
    return render(request, 'prod_detail.html', {'p': p})

def register(request):
    if(request.method == "POST"):
        u=request.POST['u']
        p = request.POST['p']
        c = request.POST['c']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        # pl = request.POST['pl']
        # n = request.POST['n']
        if(p==c):
            a=User.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l)
            a.save()
            return redirect("shop:allcat")
        else:
            return HttpResponse("passwords are not same")
    return render(request,'register.html')


def userlogin(request):
    if (request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:allcat')
        else:
            return  HttpResponse("invalid credential")
    return render(request,'login.html')



@login_required
def userlogout(request):
    logout(request)
    return redirect('shop:login')

