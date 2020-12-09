from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

def index(request):
    return render(request, 'website/base.html')

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'your-message', 'placeholder': 'Сообщение'}))

def contactView(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		#Если форма заполнена корректно, сохраняем все введённые пользователем значения
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']

			result_message = message + '\n' + name + '\n' + email

			recipients = ['ant.orlov.on@gmail.com']
			try:
				send_mail('Welcome to Omsk', result_message, 'welcometoomsk@mail.ru', recipients)
				form = ContactForm()
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			#Переходим на другую страницу, если сообщение отправлено
			return render(request, 'website/thanks.html')
	else:
		#Заполняем форму
		form = ContactForm()
	#Отправляем форму на страницу
	return render(request, 'website/index.html', {'form': form})
