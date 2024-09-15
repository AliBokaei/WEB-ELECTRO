from django.contrib import admin


# Register your models here.
from .models import Product, DiscountCode, Cart, ProductHistory, ProductVisit, CartItem, UserExtra, Offer, Category , AdditionalDetail ,Image,Review,Color
from Banner.models import Banner

admin.site.register(Offer)
admin.site.register(Color)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Review)
admin.site.register(AdditionalDetail)
admin.site.register(DiscountCode)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(UserExtra)
admin.site.register(ProductHistory)
admin.site.register(ProductVisit)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
