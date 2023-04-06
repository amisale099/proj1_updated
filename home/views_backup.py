from django.shortcuts import render, HttpResponse,redirect
from home.models import Contact

# Create your views here.
def home(request):
    return render(request,'index.html')

def homepage(request):
    return render(request,'homepage.html')

def about(request):
    #all_users=Contact.objects.all().exclude(fname='abhi')  # we are getting  objects in to x varibale from database 
    all_users=Contact.objects.all()

    print('x',all_users)         # testing purpose
    return render(request,'about.html',{'all_users':all_users})  # context object in the form of dictionary 

def contact(request,id=''):
    if request.method=='POST'and id==0:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        text  = request.POST.get('text')
        print(fname)
        print(lname)
        print(email)
        print(phone)
        print(text)
        c=Contact.objects.create(fname=fname,lname=lname,email=email,phone=phone,text=text) #contructor
        c.save()
    
        x=Contact.objects.all()
        print('x',x) 
        return render(request,'contact.html',{'x':x})
    if request.method=='POST' and id!=0:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        text  = request.POST.get('text')
        print(fname)
        print(lname)
        print(email)
        print(phone)
        print(text)
        c=Contact.objects.filter(id=id)
        c.update(fname=fname,lname=lname,email=email,phone=phone,text=text) #contructor
        # c.save()
    
        x=Contact.objects.all()
        #print('x',x) 
        return redirect('about')
    if id:
        value=Contact.objects.filter(id=id)[0]
        return render(request,'contact.html',{'value' : value,'flag':1})
    return render(request,'contact.html')
    


