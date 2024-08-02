from django.views.generic.edit import CreateView
from .models import Order
from .forms import OrderForm


# Представления для оформления заказа
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

