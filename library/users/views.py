from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
def register(request):
    if(request.method=="POST"):
        u = request.POST['u']         #username
        p = request.POST['p']         #password
        cp = request.POST['cp']     #confirm password
        e = request.POST['e']              #email
        f = request.POST['f']             #firstname
        l = request.POST['l']                #lastname
        if(p==cp):
            u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)       #create user is compliment here
            u.save()
        else:
            return HttpResponse(request,"PASSWORD SHOULD BE SAME")
        return redirect('books:home')
    return render(request,'register.html')

from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
def userlogin(request):
    if(request.method=='POST'):
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username=u,password=p)        #checks whether the details entered by user is correct or not
        if user:
            login(request,user)
            return redirect('books:home')
        else:
            return HttpResponse("INVALID USER")
    return render(request,"login.html")

def userlogout(request):
    logout(request)
    return redirect('users:login')

# def search(request):
#     return render(request,"search.html")