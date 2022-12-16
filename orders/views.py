from django.shortcuts import render

from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import Order, OrderItem


def order_create(request):
    """Create an order view"""
    cart = Cart(request)

    if request.method == "POST":
        order_form = OrderCreateForm(request.POST)
        if order_form.is_valid():
            # create order in db
            order = order_form.save()
            for item in cart:
                # create and save in single step
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
                cart.clear()  # clear cart
                return render(request, "orders/order/created.html", {"order": order})

    else:
        form = OrderCreateForm()
    return render(request, "orders/order/create.html", {"cart": cart, "form": form})
