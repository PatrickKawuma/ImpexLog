# Create your views here.
from django.shortcuts import *
from django.template import *
from sendsms import api
from django.core.mail import send_mail
from django.views.generic import TemplateView


#for sms sending
'''from sendsms.backends.base import BaseSmsBackend
from some.sms.delivery.api import *'''

def display_carrierlocalization(TemplateView):
    return render_to_response('carrierlocalization.html')

def login_user(request):
    state = "Please enter your username and password below:"
    username = ''
    password = ''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
		return redirect(carrierlocalisation)
            else:
                state = "Your account is not active, please sign up"
        else:
            state = "Your username and/or password were incorrect"

    return render_to_response('carrierlocalization.html',{'state':state, 'username':username})
   
def send_notification(request):
    state = "Create a relationship with one of the carriers. click Relate."
    return render_to_response("trytemplate.html")

def send_mail(request):
	send_mail('Subject here', 'Here is the message.', 'from@example.com',
    	['to@example.com'], fail_silently=False)


