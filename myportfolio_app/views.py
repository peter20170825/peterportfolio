from django.shortcuts import render,redirect
from myportfolio_app.models import Myportfolio,Contact
import sys
from subprocess import run,PIPE
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
#this is import statement for download
from django.http  import FileResponse
from django.conf import settings
import os





# Create your views here.
def index(request):
    my_folio = Myportfolio.objects.all()
    my_dict = {'my_folio':my_folio}
    return render(request,'myportfolio_app/index.html',context=my_dict)

def resume(request):
    return render(request,'myportfolio_app/resume.html')

def contact(request):
    if request.method == "POST":
        contact = Contact()
        name =  request.POST.get('name')
        email =  request.POST.get('email')
        subject = request.POST.get('subject')
        message =  request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()

        send_mail(
        subject+' from '+name+' whose email is: '+email, #title
        message, #message
        'settings.EMAIL_HOST_USER',#sender
        ['peter_modo@yahoo.com',], #receiver
        fail_silently=False)
        # return HttpResponse('<h1> Thanks for contacting us </h1>')
        return redirect('thankyou')

    return render(request,'myportfolio_app/contact.html')


def thankyou(request):
    return render(request,'myportfolio_app/thankyou.html')


def ImagePage(request,id):
    my_image = Myportfolio.objects.get(id=id)
    return render(request,'myportfolio_app/image.html',{'my_image':my_image})



def download(request,id):
    #get a reference to the file
    file =os.path.join(settings.BASE_DIR,'download/Guess_Number_App.exe')

    #open the file
    fileOpened = open(file,'rb')

    #return the file using FileResponse
    return FileResponse(fileOpened)
