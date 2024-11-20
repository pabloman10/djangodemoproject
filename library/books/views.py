from django.db.models import Q
from django.shortcuts import render,redirect
from books.models import Book
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required
def addbooks(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        pa=request.POST['pa']
        l=request.POST['l']
        c=request.FILES['c']
        pd=request.FILES['pd']
        b=Book.objects.create(title=t,author=a,pages=pa,price=p,language=l,cover=c,pdf=pd)      #creates a new record
        b.save()
        return redirect('books:view')#save the records inside the table book
    return render(request,'add.html')
@login_required
def viewbooks(request):
    k=Book.objects.all()  #Reads all records from table Book.
    context={'book':k}      #passes data from views to html file.context is dictionary type.
    return render(request,'view.html',context)

def details(request,p):
    b=Book.objects.get(id=p)
    context={'book':b}
    return render(request,'details.html',context)

def edit(request,p):
    b=Book.objects.get(id=p)
    if (request.method == "POST"):
        b.title=request.POST['t']
        b.author=request.POST['a']
        b.price=request.POST['p']
        b.pages=request.POST['pa']
        b.language=request.POST['l']
        if(request.FILES.get('c')==None):
            b.save()
        else:
            b.cover=request.FILES.get('c')
        if(request.FILES.get('pd')==None):
            b.save()
        else:
            b.pdf=request.FILES.get('pd')

        b.save()
        return redirect('books:view')
    context={'book':b}
    return render(request,'edit.html',context)

def delete(request,p):
    b=Book.objects.get(id=p)
    b.delete()
    return redirect('books:view')

def search(request):
    b=None
    if(request.method=="POST"):
        print("hello")
        query=request.POST['q']
        print(query)
        if query:
            b=Book.objects.filter(Q(title=query) | Q(author=query))
    return render(request,"search.html",{'book':b})