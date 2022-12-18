from cart.cart import Cart
from django.shortcuts import redirect, render
from django.urls import reverse

from orders.forms import OrderCreateForm
from orders.models import Order, OrderItem
from orders.tasks import order_created


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
                # asynchronous task to send email
                order_created.delay(order.id)
                # set order insession
                request.session["order_id"] = order.id
                # go to payment
                return redirect(reverse("payment:process"))
                # return render(request, "orders/order/created.html", {"order": order})

    else:
        form = OrderCreateForm()
    return render(request, "orders/order/create.html", {"cart": cart, "form": form})
