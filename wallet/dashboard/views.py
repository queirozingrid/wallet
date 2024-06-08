from django.shortcuts import render
from dashboard.forms import AddWalletForm
from dashboard import models
# Create your views here.

def add_wallet(request):
    form = None
    if request.GET.get('form'):
        form = request.GET.get('form')

    else:
        form = AddWalletForm()

    if request.method == 'POST':
        label = request.POST.get('wallet_label')
        amount = request.POST.get('wallet_amount')

        form = AddWalletForm({'label': label, 'amount': amount})
        if form.is_valid():
            form.save()

    context = {
        'form': form,
        'title': 'Dashboard'
    }
    return render(request, 'templates/base.html', context)