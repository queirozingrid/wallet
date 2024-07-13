from django.shortcuts import render
from dashboard.forms import AddWalletForm
from dashboard import models
from django.http import HttpResponseRedirect

def add_wallet(request):
    form = None
    if request.method == 'GET':
        form = AddWalletForm()

    elif request.method == 'POST':
        label = request.POST.get('label')
        amount = request.POST.get('amount')

        form = AddWalletForm({'label': label, 'amount': amount})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')

    context = {
        'form': form,
        'title': 'Dashboard'
    }
    return render(request, 'templates/table_pages.html', context)

def list_wallets(request):
    all_wallets = models.Wallet.objects.all()
    context = {
        'wallets': all_wallets
    }
    return render(request, 'templates/table_pages.html', context)

def list_transactions(request):
    all_transactions = models.Transaction.objects.all()
    context = {
        'transactions': all_transactions
    }
    return render(request, 'templates/table_pages.html', context)