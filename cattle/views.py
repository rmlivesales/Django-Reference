from django.shortcuts import render
from django.utils import timezone
from .models import Sale_Bill, Purchase
# from .forms import PostForm

# My views
def bill_view(request):
    bill = Sale_Bill.objects.all()[0]
    purchases = Purchase.objects.filter(bill=bill)
    heads = 0
    weight = 0
    amount = 0
    for p in purchases:
        heads += p.no_head
        weight += p.weight
        amount += p.amount
    av_weight = weight/heads
    av_price = amount*100/weight
    total = amount\
        + (bill.commission if bill.commission else 0)\
        + (bill.feed if bill.feed else 0)\
        + (bill.freight if bill.freight else 0)\
        + (bill.other if bill.other else 0)\
        + 0
    return render(request, 'cattle/bill_view.html', {\
        'bill': bill,\
        'purchases': purchases,\
        'heads': heads,\
        'weight': weight,\
        'amount': amount,\
        'av_weight': av_weight,\
        'av_price': av_price,\
        'total': total,\
        })
