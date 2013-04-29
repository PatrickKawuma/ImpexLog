from django import forms
from sendsms import api


class RelationshipForm(forms.Form):
	
  
    def send_sms(request):
        try:
            api.send_sms(body='Kindly requesting you to carry my cargo', from_phone='+256776713008', to=['+256775430593'])
            state = "blah blah has received the notification on their phone."

        except:
            return "can't send message"


