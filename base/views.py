from django.shortcuts import render, redirect
from .models import Client, Transaction, Change
from .forms import ClientsForm
from django.db.models import Sum


def index(request):
    return render(request, 'base/index.html')


def show_clients(request):
    clients = Client.objects.filter(user_status='active')
    data = {
        'clients': clients
    }
    return render(request, 'base/clients.html', data)


def add_clients(request):
    error = ''

    if request.method == 'POST':
        form = ClientsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/show/')
        else:
            error = 'Некорректные данные'

    form = ClientsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'base/add_clients.html', data)


def show_client(request, userid):
    client = Client.objects.get(id=userid)
    order = Transaction.objects.filter(client_id=userid, status_transaction='confirm').aggregate(Sum('price'))
    if request.method == 'POST':
        Client.objects.filter(id=userid).update(user_status='delete')
        change = Change(name=client.name, surname=client.surname, middle_name=client.middle_name, user_status='delete')
        change.save()
        return redirect('/')
    return render(request, 'base/client.html', {'client': client, 'order': order['price__sum']})


