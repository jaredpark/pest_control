from django import forms

class ContactForm(forms.Form):
	error_css_class = 'error'
	required_css_class = 'required'
	first_name = forms.CharField(label='First Name', required=True)
	last_name = forms.CharField(label='Last Name', required=True)
	address = forms.CharField(label='Street Address', required=False)
	zipcode = forms.IntegerField(label='Zip Code', required=False)
	phone = forms.CharField(label='Phone Number', required=True)
	email = forms.EmailField(label='Email Address', required=True)
	preferred_contact = forms.ChoiceField(label='Preferred contact', choices=(('phone', 'phone'), ('email', 'email')))
	availability = forms.ChoiceField(label='When are you available?', choices=(('Evening', '4pm to 8pm'), ('Afternoon', 'noon to 4pm'), ('Morning', '8am to noon')))
	service = forms.ChoiceField(label='What type of service do you need?', choices=(('General Home Inspection', 'General Home Inspection'), ('Termites', 'Termites'), ('Scorpions', 'Scorpions'), ('Bed Bugs', 'Bed Bugs'), ('Other', 'Other Specific Pest (please specify in message)'), ('None', 'General Information (please specify in message)')))
	permission = forms.BooleanField(label="Do you want to know the 5 things your bug guy isn't telling you?", required=False, initial=True)
	subject = forms.CharField(label='Subject', initial='Request an Estimate')
	message = forms.CharField(label='Message', max_length=400, initial='Please provide any additional information here.',
		widget = forms.Textarea())