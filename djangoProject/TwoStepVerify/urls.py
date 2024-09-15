from django.urls import path

from SignUp.views import register
from TwoStepVerify.views import activate_user

urlpatterns = [
    path('register/', register, name='register'),
    path('accounts/activate/<activation_key>/', activate_user, name='activate_user'),
    # ... (مسیرهای دیگر)
]