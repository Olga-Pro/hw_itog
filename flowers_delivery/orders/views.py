from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from catalog.models import Flower
from .models import Order


@login_required
def create_order(request, flower_id):
    flower = Flower.objects.get(id=flower_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        order = Order(user=request.user, flower=flower, quantity=quantity)
        order.save()
        return redirect('flower_list')
    return render(request, 'orders/create_order.html', {'flower': flower})


def order_success(request):
    return render(request, 'orders/order_success.html')
