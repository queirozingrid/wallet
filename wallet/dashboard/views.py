from django.shortcuts import render, redirect
from dashboard.forms import AddWalletForm
from dashboard import models
from django.http import HttpResponseRedirect
from django.contrib import messages

def add_wallet(request):
    label = request.POST.get('label')
    amount = request.POST.get('amount')

    form = AddWalletForm({'label': label, 'amount': amount})
    if form.is_valid():
        form.save()
        messages.success(request, 'Wallet added successfully!')
    else:
        errors = form.errors.values()
        for error in errors:
            messages.error(request, error)

    return redirect('/wallet')

def list_wallets(request):
    all_wallets = models.Wallet.objects.all()

    form = AddWalletForm()
    
    context = {
        'wallets': all_wallets,
        'title': 'Wallets Management',
        'form': form,
        'action': 'add_wallet/'
    }
    return render(request, 'templates/table_pages.html', context)

def delete_wallet(request):
    wallet_id = request.GET.get('id')
    wallet = models.Wallet.objects.get(id=wallet_id)

    try:
        wallet.delete()
        messages.success(request, 'Wallet deleted successfully!')
    except Exception as e:
        messages.error(request, 'It wasn\'t possible to delete this wallet: {}'.format(e))

    return redirect('/wallet')

def list_transactions(request):
    all_transactions = models.Transaction.objects.all()
    context = {
        'transactions': all_transactions
    }
    return render(request, 'templates/table_pages.html', context)