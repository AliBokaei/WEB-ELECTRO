from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from pyexpat.errors import messages

from Banner.models import Banner
from StoreApp.models import Category, Offer


# Create your views here.
def register(request):

    categories = Category.objects.all()
    banner1 = Banner.objects.get(title="banner1")
    banner2 = Banner.objects.get(title="banner2")
    offer1 = Offer.objects.get(title="offer1")
    offer2 = Offer.objects.get(title="offer2")

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            # form.save()
            return render(request, 'Front/Welcome.htm')
            # return render(request, "Front/index.htm", {'show_modal': True,
            #             'banner1': banner1, 'banner2': banner2,'categories':categories ,
            #             'offer1':offer1, 'offer2':offer2 })
        else:

            # for field, errors in form.errors.items():
            #     print(f"Error for field {field}: {errors}")

            # messages.error(request, 'Please correct the errors below.')
            errors = form.errors.items()
            context = {
                'errors': errors  # Add the errors to the context
            }

            return render(request, 'Front/notCorrectInfo.htm', context)


    else:
        form = UserCreationForm()

    return render(request, 'Front/index.htm', {'banner1': banner1, 'banner2': banner2 ,'categories':categories,
                        'offer1':offer1, 'offer2':offer2 })
    #return render(request, 'Front/index.htm')