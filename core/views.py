from django.shortcuts import render, redirect
from django.contrib.auth import logout

from item.models import Category, Item

from .forms import SignupForm


from django.shortcuts import get_object_or_404, redirect
from item.models import Item, Cart, CartItem

def add_to_cart(request, item_id):
    # Get the item
    item = get_object_or_404(Item, pk=item_id)

    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if the item is already in the cart
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, item=item)

    # If the item was already in the cart, increase its quantity
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/cart/')  # Assuming you have a URL named 'cart' for the cart page

def view_cart(request):
    # Get the user's cart if authenticated, otherwise create an empty cart
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart = None
    price = 0
    
    for item in cart.items.all():
        price += item.price
   

    return render(request, 'core/cart.html', {'price': price, 'cart': cart})

def cart_delete(request, id):
    cart_item = get_object_or_404(CartItem, id=id)
    print(cart_item)
    cart_item.delete()
    return redirect("/cart/")
    # return render(request, "core/base.html")

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def logout_view(request):
    logout(request)
    return redirect('/dashboard/')

# def order_placed(request):
    
#     return redirect('/order_placed/')
