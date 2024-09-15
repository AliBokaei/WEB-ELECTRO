from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from Banner.models import Banner
from StoreApp.models import Category, Offer, Product, AdditionalDetail, CartItem, Cart
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def home(request):

    categories = Category.objects.all()
    banner1 = Banner.objects.get(title="banner1")
    banner2 = Banner.objects.get(title="banner2")
    offer1 = Offer.objects.get(title="offer1")
    offer2 = Offer.objects.get(title="offer2")
    # Our Bestseller Products
    offerBigBestseller = Offer.objects.get(title="offerBigBestseller")
    offerminiBestseller1 = Offer.objects.get(title="offerminiBestseller1")
    offerminiBestseller2 = Offer.objects.get(title="offerminiBestseller2")
    offerminiBestseller3 = Offer.objects.get(title="offerminiBestseller3")
    offerminiBestseller4 = Offer.objects.get(title="offerminiBestseller4")
    offerminiBestseller5 = Offer.objects.get(title="offerminiBestseller5")
    offerminiBestseller6 = Offer.objects.get(title="offerminiBestseller6")

    user_details(request)
    login_show_element = False
    if request.user.is_authenticated:
        login_show_element = True

    context = {'banner1': banner1,
               'banner2': banner2 ,
               'categories':categories,
               'offer1':offer1,
               'offer2':offer2,
               'login_show_element': login_show_element,
               'offerBigBestseller':offerBigBestseller,
               'offerminiBestseller1':offerminiBestseller1,
               'offerminiBestseller2':offerminiBestseller2,
               'offerminiBestseller3':offerminiBestseller3,
               'offerminiBestseller4':offerminiBestseller4,
               'offerminiBestseller5':offerminiBestseller5,
               'offerminiBestseller6':offerminiBestseller6,

    }

    return render(request, 'Front/index.htm', context)


def productDetail(request, product_id=None):
    global login_show_element
    try:
        product = Product.objects.get(pk=product_id)

        # Check if additionaldetail exists using a safe method
        try:
            additional_details = product.additionaldetail
            images = additional_details.additional_images.all()
        except Product.additionaldetail.RelatedObjectDoesNotExist:
            additional_details = None  # Set to None if not found
            images = []  # Set images to an empty list

    except Product.DoesNotExist:
        product = None
        additional_details = None
        images = []

    if request.user.is_authenticated:
        login_show_element = True
    else:
        login_show_element = False
    context = {'product': product or {}, 'images': images , "login_show_element": login_show_element}
    return render(request, 'Front/indexProductDetail.htm', context)


def user_details(request):
    if request.user.is_authenticated:
        user = request.user  # Access user information after successful login
        # Print user details (avoid printing directly in a production environment)
        print(f"User: {user.username}, Email: {user.email}")  # Replace with your desired output
        # You can access other user attributes as needed (e.g., user.first_name, user.last_name)

        # Optionally, pass user details to a template for display:
        # context = {'user': user}
        # return render(request, 'user_details.htm', context)
    else:
        # Redirect to login page if not authenticated
        print(f"User Not Logged In")
        # return redirect('login_url')  # Replace with your login URL pattern name

    # Handle other logic for authenticated users here
    # return render(request, 'user_details.htm')  # Example page to display user details



@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')

        # Validate product ID and user
        try:
            product = Product.objects.get(pk=product_id)
            cart, created = Cart.objects.get_or_create(user=request.user)
        except (Product.DoesNotExist, Cart.DoesNotExist):
            # Handle product or cart not found errors (e.g., log or redirect)
            return redirect('error_page')  # Replace with appropriate error handling

        # Check if item already exists in cart
        cart_item = cart.items.filter(product=product).first()
        if cart_item:
            cart_item.quantity += 1
            cart_item.save()
        else:
            CartItem.objects.create(cart=cart, product=product)

        return redirect('cart_view')  # Redirect to cart view after successful addition

    else:
        return redirect('home_page')  # Redirect to homepage for non-POST requests

def cart_view(request):
    cart = request.user.cart  # Assuming a one-to-one relationship between User and Cart
    cart_items = cart.items.all