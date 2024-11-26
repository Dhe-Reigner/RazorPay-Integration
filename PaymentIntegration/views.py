from django.shortcuts import render
from . models import Coffee

import razorpay


# Create your views here.
# def home(request):
#     all_mug = Coffee.objects.all()
#     return render(request, 'index.html',{
#         'mug':all_mug
#     })


# def home(request):
#     if request.method == "POST":
#         coffee_name = request.POST.get('coffee_name')
#         coffee_amount = request.POST.get('coffee_amount')
#         payment_id = request.POST.get('payment_id')
#         Coffee.objects.create(name=coffee_name, amount=coffee_amount, payment_id=payment_id, paid=True)
#         return render(request,'success.html')
#     return render(request, 'home.html')

def home(request):
    if request.method  == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        client = razorpay.Client(auth = ())
        print(name + amount)
def success(request):
    return render(request, 'success.html')