from django.shortcuts import render , redirect
from .models import Register
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .forms import DocumentForm
from zeal.settings import EMAIL_HOST_USER


# Create your views here.

def register(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            subject1 = "Your request has been submitted successfully"
            message1 = "Thanks for showing interset in ZEAL society. Your application is under review. You will be informed after the review period. BEST OF LUCK"
            from_email = request.POST.get('email')
            subject2 = "New request received"
            message2 = "New request is received from " + request.POST.get("name") + "  Branch : "+ request.POST.get("branch")  + " Year : " + request.POST.get("year") +" ."
            if from_email:
                send_mail(subject1, message1, EMAIL_HOST_USER, [from_email])
                send_mail(subject2, message2, EMAIL_HOST_USER, [EMAIL_HOST_USER])
            return redirect('home')
    else:
        form=DocumentForm()    
   
    return render(request,'register.html',{'form':form})

        


        
    
    
    
        
    

def about(request):

    return render(request,'about.html')