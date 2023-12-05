from django.shortcuts import render, redirect
from dev.forms import ContactForm
from dev.forms import RegisterForm


def index(request):
    context = {'nome': 'Ricardo'}
    return render(request, 'index.html', context)


def nome(request, nome):
    context = {'nome': nome}
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get("subject")
            message = form.cleaned_data.get("message")
            sender = form.cleaned_data.get("sender")
            cc_myself = form.cleaned_data.get("cc_myself")

            recipients = ['grrodrigues@restinga.ifrs.edu.br']
            if cc_myself:
                recipients.append(sender)
            #send_email(subject, message, sender, recipients)

            context = {
                'form': form,
            }
            return render(request, 'obrigado.html', context)
    else:
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contato.html', context)

def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(response, 'registration/register.html', context)
