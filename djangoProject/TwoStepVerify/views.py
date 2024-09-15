import uuid
from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.http import request
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from TwoStepVerify.models import User


# Create your views here.
def register(request, user=None):
    # ... (ایجاد کاربر جدید - قسمت قبلاً نوشته شده است)

    activation_key = uuid.uuid4()
    user.is_active = False
    user.activation_key = activation_key
    user.save()

    # ارسال ایمیل تأیید
    send_activation_email(user)

    # ... (پیام موفقیت یا اقدامات بعدی)
    return redirect('register_success')

def activate_user(request, activation_key):
    try:
        user = User.objects.get(activation_key=activation_key)
    except User.DoesNotExist:
        # ... (مدیریت کاربر نامعتبر)
        return

    user.is_active = True
    user.save()

    # ... (هدایت به صفحه ورود به سیستم)
    return redirect('login')


def send_activation_email(user):
    activation_key = user.activation_key
    activation_link = f"http://{request.get_host()}/accounts/activate/{activation_key}"

    subject = "Activate Your Account"
    body = f"Hi {user.username},\n\nPlease click on the following link to activate your account:\n{activation_link}"

    send_mail(
        subject,
        body,
        DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )