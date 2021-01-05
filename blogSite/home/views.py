from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def about(request):
    return render(request,'home/about.html')
    #return HttpResponse('this is about')

def home(request):
    return render(request,'home/index.html')
    #return HttpResponse('this is home')

def contact(request):
    #messages.error(request, 'Welcome to the blog.')
    if request.method == 'POST':
        namE = request.POST['name']
        emaiL = request.POST['email']
        msg = request.POST['message']
        if len(namE) <2 or len(emaiL) <4 or len(msg) < 5:
            messages.error(request, 'Please enter Valid information!!')

        else:
            details = Contact(name = namE,email = emaiL,message = msg)
            details.save()
            messages.success(request, 'Form submited Succesfully!!.')
    return render(request,'home/contact.html')
    