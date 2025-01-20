from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from base import models
from base.models import Contact
# Create your views here.
# def home(request):
#     return HttpResponse("Hello suraj")

# def home(request):
#     return render(request,'home.html')

def contact(request):
    if request.method== "POST":

        print('post')
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        content=request.POST.get('content')
        print(name,number,contact)
        if len(name)>1 and len(name)<30:
           pass
        else:
             messages.error(request,'Lenght of name shuold be greater than 2 and less than 30 words')
             return render(request,'home.html')
        if len(name)>1 and len(email)<30:
            pass
        else:
            messages.error(request,'Invalid email try again')
            return render(request,'home.html')
        
        if len(number)>2 and len(number)<13:
            pass
        else:
             messages.error(request,'Invalid number try again')
             return render(request,'home.html')
        ins=models.Contact(name=name,email=email,content=content,number=number)
        ins.save()
        messages.success(request,'Thank you for contacting me ! your message hava been saved')
        print('date has been save to database')
        print('the request is no pass')
    return render(request,'home.html') 
        


        




