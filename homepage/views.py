from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from pest_control.forms import ContactForm
from django.core.mail import send_mail
from context_processors import site_settings_processor

def homepage(request):
	context_dictionary = {}
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ContactForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# try:
				first_name = form.cleaned_data['first_name']
				last_name = form.cleaned_data['last_name']
				address = form.cleaned_data['address']
				zipcode = form.cleaned_data['zipcode']
				phone = form.cleaned_data['phone']
				sender = form.cleaned_data['email']
				subject = form.cleaned_data['subject']
				subject = subject + '-' + first_name + ' ' + last_name
				message = form.cleaned_data['message']
				recipients = [site_settings_processor(request)['site_email'],]
				fullemail = first_name + " " + last_name + " " + "<" + sender + ">"
				send_mail(subject, message, fullemail, recipients, fail_silently=False)
				context_dictionary = {'first_name': form.cleaned_data['first_name'], }
				return(render(request, 'homepage/index.html', context_dictionary))
			# except BaseException as e:
			# 	context_dictionary = { 'first_name': str(e), }
			# 	return(render(request, 'homepage/index.html', context_dictionary))
		else:
			context_dictionary = { 'form_errors': form.errors, 'form': form, }
			return(render(request, 'homepage/index.html', context_dictionary))
	# if a GET (or any other method) we'll create a blank form
	else:
		form = ContactForm()
		context_dictionary = {'form': form, }
		return(render(request, 'homepage/index.html', context_dictionary))

def about(request):
	context_dictionary = {}
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ContactForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# try:
				first_name = form.cleaned_data['first_name']
				last_name = form.cleaned_data['last_name']
				address = form.cleaned_data['address']
				zipcode = form.cleaned_data['zipcode']
				phone = form.cleaned_data['phone']
				sender = form.cleaned_data['email']
				subject = form.cleaned_data['subject']
				subject = subject + '-' + first_name + ' ' + last_name
				message = form.cleaned_data['message']
				recipients = [site_settings_processor(request)['site_email'],]
				fullemail = first_name + " " + last_name + " " + "<" + sender + ">"
				send_mail(subject, message, fullemail, recipients, fail_silently=False)
				context_dictionary = {'first_name': form.cleaned_data['first_name'], }
				return(render(request, 'about.html', context_dictionary))
			# except BaseException as e:
			# 	context_dictionary = { 'first_name': str(e), }
			# 	return(render(request, 'homepage/index.html', context_dictionary))
		else:
			context_dictionary = { 'form_errors': form.errors, 'form': form, }
			return(render(request, 'about.html', context_dictionary))
	# if a GET (or any other method) we'll create a blank form
	else:
		form = ContactForm()
		context_dictionary = {'form': form, }
		return(render(request, 'about.html', context_dictionary))

def products(request):
	context_dictionary = {}
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ContactForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# try:
				first_name = form.cleaned_data['first_name']
				last_name = form.cleaned_data['last_name']
				address = form.cleaned_data['address']
				zipcode = form.cleaned_data['zipcode']
				phone = form.cleaned_data['phone']
				sender = form.cleaned_data['email']
				subject = form.cleaned_data['subject']
				subject = subject + '-' + first_name + ' ' + last_name
				message = form.cleaned_data['message']
				recipients = [site_settings_processor(request)['site_email'],]
				fullemail = first_name + " " + last_name + " " + "<" + sender + ">"
				send_mail(subject, message, fullemail, recipients, fail_silently=False)
				context_dictionary = {'first_name': form.cleaned_data['first_name'], }
				return(render(request, 'about.html', context_dictionary))
			# except BaseException as e:
			# 	context_dictionary = { 'first_name': str(e), }
			# 	return(render(request, 'homepage/index.html', context_dictionary))
		else:
			context_dictionary = { 'form_errors': form.errors, 'form': form, }
			return(render(request, 'about.html', context_dictionary))
	# if a GET (or any other method) we'll create a blank form
	else:
		form = ContactForm()
		context_dictionary = {'form': form, }
		return(render(request, 'products.html', context_dictionary))

def contact(request):
	context_dictionary = {}
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ContactForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# try:
				first_name = form.cleaned_data['first_name']
				last_name = form.cleaned_data['last_name']
				address = form.cleaned_data['address']
				zipcode = form.cleaned_data['zipcode']
				phone = form.cleaned_data['phone']
				sender = form.cleaned_data['email']
				subject = form.cleaned_data['subject']
				subject = subject + '-' + first_name + ' ' + last_name
				message = form.cleaned_data['message']
				recipients = [site_settings_processor(request)['site_email'],]
				fullemail = first_name + " " + last_name + " " + "<" + sender + ">"
				send_mail(subject, message, fullemail, recipients, fail_silently=False)
				context_dictionary = {'first_name': form.cleaned_data['first_name'], }
				return(render(request, 'about.html', context_dictionary))
			# except BaseException as e:
			# 	context_dictionary = { 'first_name': str(e), }
			# 	return(render(request, 'homepage/index.html', context_dictionary))
		else:
			context_dictionary = { 'form_errors': form.errors, 'form': form, }
			return(render(request, 'about.html', context_dictionary))
	# if a GET (or any other method) we'll create a blank form
	else:
		form = ContactForm()
		context_dictionary = {'form': form, }
		return(render(request, 'contact.html', context_dictionary))