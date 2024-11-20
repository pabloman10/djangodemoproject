from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from shop.models import Category,Product

def Home(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'home.html',context)
def Products(request,i):
    c=Category.objects.get(id=i)
    p=Product.objects.filter(Category=c)
    context={'cat':c, 'pro':p}
    return render(request,'products.html',context)
def ProductDetail(request,i):
    c=Product.objects.get(id=i)
    context={'pro':c}
    return render(request,'detail.html',context)
def register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        if (p == cp):
            u = User.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l)
            u.save()
        else:
            return HttpResponse(request, "PASSWORD SHOULD BE SAME")
            return redirect('shop:Home')
    return render(request,'register.html')
def u_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']

        user = authenticate(username=u, password=p)

        if user:
            login(request,user)
            return redirect('shop:Home')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request, 'login.html')


@login_required
def u_logout(request):
    logout(request)
    return redirect('shop:Home')

def addcategories(request):
    if (request.method == "POST"):
        n= request.POST['n']
        d= request.POST['d']
        i = request.FILES['i']
        b =Category.objects.create(name=n,desc=d,image=i)
        b.save()
        return redirect('shop:addcategories')
    return render(request,'Addcategory.html')
def addproducts(request):
    if (request.method == "POST"):
        n = request.POST['n']
        d = request.POST['d']
        i = request.FILES.get('i')
        s = request.POST['s']
        p = request.POST['p']
        c = request.POST['c']
        cat=Category.objects.get(name=c)
        b = Product.objects.create(name=n, desc=d, image=i,stock=s,price=p,category=cat)
        b.save()
        return redirect('shop:addproducts')
    return render(request,'Addproduct.html')
def addstock(request,i):
    p=Product.objects.get(id=i)
    if(request.method=="POST"):
        p=request.POST['n']
        p.save()
        return redirect('shop:ProductDetail')
    context={'pro':p}
    return render(request,'addstock.html',context)




