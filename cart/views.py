from django.shortcuts import render, redirect, reverse
import sweetify


def view_cart(request):
    """
    A view that renders the cart contents page
    """
    return render(request, "cart.html")


def add_item_to_cart(request, id):
    """
    Add a quantity of the specified product to the cart
    """
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    """
    If statement that ensures a customer can't add/create
    duplicates of the same product to the shopping cart
    """
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    sweetify.success(request,
                     """Your selection has been added
                     to your shopping cart!""",
                     icon="success")
    return redirect(reverse('view_cart'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified
    product to the specified amount
    """
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    sweetify.success(request,
                     """Successfully removed from
                     your shopping cart!""",
                     icon="success")
    return redirect(reverse('view_cart'))
