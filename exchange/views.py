from django.shortcuts import render
from .service import current_exchanges


def index(request):
    currencies = current_exchanges()

    if request.method == 'GET':
        context = {
            'currencies': currencies,
        }
        return render(request, template_name='exchange/index.html',
                      context=context)

    if request.method == 'POST':
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')
        amount = request.POST.get('from-amount')
        converted_amount = round(
            currencies[to_curr] / currencies[from_curr] * float(amount), 2
        )
        context = {
            'currencies': currencies,
            'from_curr': from_curr,
            'to_curr': to_curr,
            'amount': amount,
            'converted_amount': converted_amount
        }
        return render(request, template_name='exchange/index.html',
                      context=context)
