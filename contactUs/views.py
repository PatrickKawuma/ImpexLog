# Create your views here.
from django.template import *
from django.shortcuts import *
from contactUs.forms import *


def contact(request):
    if request.method == 'POST':
	form = ContactForm(request.POST)
    else:
	form = ContactForm()
	return render_to_response('contactUs.html', {'form': form})
