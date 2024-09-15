from django.shortcuts import redirect, render

from StoreApp.models import Review


def submit_review(request):
  if request.method == 'POST':
    # Get the submitted rating value
    rating = request.POST.get('rating')
    name = request.POST.get('name')
    email = request.POST.get('email')
    descriptions = request.POST.get('descriptions')
    # Additional form data processing (optional)
    # You can access other form fields using request.POST.get('field_name')

    # Save the rating data to the database (replace with your model logic)
    # This example assumes you have a model named Rating
    rating_obj = Review.objects.create(user=request.user, email=email, name=name, rating=rating, description=descriptions)
    print(rating_obj)
    # Handle successful submission (e.g., redirect to a confirmation page)
    return render(request, 'Front/Welcome.htm')

  else:
    # Handle GET requests (e.g., display an error message)
    return redirect('error_url')  # Replace 'error_url' with your desired URL