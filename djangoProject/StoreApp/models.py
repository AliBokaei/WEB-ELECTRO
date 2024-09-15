from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from Banner.models import Banner


class UserExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    cart = models.OneToOneField("Cart", on_delete=models.CASCADE, blank=True, null=True)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"



class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photos = models.ImageField(upload_to='products/')
    videos = models.FileField(upload_to='products/videos/', blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title



class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/additional/')


class Color(models.Model):
    # Name of the color
    name = models.CharField(max_length=255, unique=True)

    # Hexadecimal code for the color
    hex_code = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return f"{self.name} (#{self.hex_code})"





class DiscountCode(models.Model):
    code = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    discount_type = models.CharField(max_length=20, choices=[('percentage', 'Percentage'), ('amount', 'Amount')])
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    max_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    products = models.ManyToManyField('Product', blank=True)
    categories = models.ManyToManyField('Category', blank=True)
    apply_to_all = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class ProductHistory(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()

class ProductVisit(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    visit_date = models.DateField()
    count = models.PositiveIntegerField()
    def __str__(self):
        return self.product


# Create your models here.
class Offer(models.Model):
    title = models.CharField(max_length=200)
    header = models.CharField(max_length=200)  # h1
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_photo = models.ImageField(upload_to='offers/')

    def __str__(self):
        return f"{self.title} - {self.product.title} - {self.discount_percentage}% Off"



class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        blank=True,
        null=True
    )
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    class Meta:
        unique_together = ('name', 'parent')
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def clean(self):
        # Ensure the depth does not exceed 5 levels
        if self.parent:
            parent = self.parent
            depth = 1
            while parent.parent:
                parent = parent.parent
                depth += 1
                if depth >= 5:
                    raise ValidationError('Maximum category depth is 5.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


from django.db import models
from django.contrib.auth import get_user_model

class Review(models.Model):
    # Title of the review

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)

    # User who submitted the review
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # Rating from 1 to 5
    rating = models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])

    # Date and time the review was submitted
    review_date = models.DateTimeField(auto_now_add=True)

    # Flag to indicate if the review needs moderation (True) or is approved (False)
    is_approved = models.BooleanField(default=False)

    # Body of the review
    descriptions = models.TextField()

    def __str__(self):
        return f"Review by {self.reviewer.username} on {self.review_date} for {self.product.title}"


class SimilarProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    score = models.FloatField(blank=True, null=True)  # Optional similarity score
    reason = models.TextField(blank=True)  # Optional reason for recommendation


class AdditionalDetail(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)  # One-to-One relationship with Product

    # Colors (using ManyToManyField to Color model)
    colors = models.ManyToManyField(Color, blank=True)

    # Reviews
    # Consider using a separate app for reviews to manage them more effectively
    reviews = models.ForeignKey(Review, on_delete=models.SET_NULL, blank=True, null=True)

    # Stock
    stock_count = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])  # Positive integer for stock count

    # Additional Images
    additional_images = models.ManyToManyField(Image, blank=True)

    # Brand
    brand = models.CharField(max_length=255, blank=True)

    # Dimensions
    item_height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Decimal field for height
    item_width = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Decimal field for width

    # Screen Size (if applicable)
    screen_size = models.CharField(max_length=255, blank=True)
    # Model Number
    model_number = models.CharField(max_length=255, blank=True)

    ram_size = models.CharField(max_length=255, blank=True)  # String for screen size
    # Operating System (if applicable)
    operating_system = models.CharField(max_length=255, blank=True)

    # Similar Products
    # Consider using a ManyToManyField relationship with a separate Product model for similar products
    similar_products = models.ManyToManyField(Product, related_name='similar_on', blank=True)

    def __str__(self):
        return f"Additional details for {self.product.title}"


