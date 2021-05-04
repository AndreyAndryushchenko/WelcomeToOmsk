from .models import Sight
from .forms import ContactForm
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError


def index(request):
    sights_list = Sight.objects.order_by('id')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            result_message = message + '\n' + name + '\n' + email

            anton = 'ant.orlov.on@gmail.com'

            recipients = [anton]
            try:
                send_mail('Welcome to Omsk', result_message, 'welcometoomsk@mail.ru', recipients)
                form = ContactForm()
                return HttpResponseRedirect('/thanks/')
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
    else:
        form = ContactForm()

    data = {
        'sights_list': sights_list,
        'form': form,
    }

    return render(request, 'website/base.html', data)


def detail(request, sight_id):
    try:
        s = Sight.objects.get(id=sight_id)
    except:
        raise Http404('Запись о достопримечательности не найдена')

    return render(request, 'website/detail.html', {'sight': s})


def thanks(request):
    return render(request, 'website/thanks.html')
