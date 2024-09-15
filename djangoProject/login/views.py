from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from Banner.models import Banner
from StoreApp.models import Category, Offer
from StoreApp.views import user_details


# Create your views here.
def loginView(request):
    categories = Category.objects.all()
    banner1 = Banner.objects.get(title="banner1")
    banner2 = Banner.objects.get(title="banner2")
    offer1 = Offer.objects.get(title="offer1")
    offer2 = Offer.objects.get(title="offer2")

    context = {'banner1': banner1, 'banner2': banner2, 'categories': categories,
               'offer1': offer1, 'offer2': offer2}

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Login HERE
            login(request, form.get_user())
            # print("User :" + "logged in")
            user_details(request)
            return render(request, 'Front/Welcome.htm')
        else:
            errors = form.errors.items()
            context2 = {
                'errors': errors  # Add the errors to the context
            }
            return render(request, 'Front/notCorrectInfo.htm', context2)
            # for field, errors in form.errors.items():
            #     print(f"Error for field {field}: {errors}")
    else:
        form = AuthenticationForm()

    return render(request, 'Front/index.htm', context)
    #return render(request, 'Front/index.htm')
