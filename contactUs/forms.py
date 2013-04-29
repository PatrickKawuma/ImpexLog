from django import forms

TOPIC_CHOICES = (
	('general', 'General enquiry'),
	('reliability', 'reliability'),
	('transit times', 'reliability'),
)

class ContactForm(forms.Form):
	#Name = forms.CharField(widget=forms.Textfield())
	Topic = forms.ChoiceField(choices=TOPIC_CHOICES)
	Message = forms.CharField(widget=forms.Textarea())
	Email_address = forms.EmailField(required=False)



