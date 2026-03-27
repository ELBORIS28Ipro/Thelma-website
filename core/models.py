from django.db import models
from django.utils.text import slugify


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)
    cta_text = models.CharField(max_length=50, default='Learn More')
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('press_on', 'Press-On Nails'),
        ('custom', 'Custom Set'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    currency = models.CharField(max_length=5, default='XAF')
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='press_on')
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    duration = models.CharField(max_length=50, blank=True)
    best_for = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class GalleryPhoto(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.caption or f"Photo {self.pk}"


class BookingInquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    service = models.CharField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name_plural = 'Booking Inquiries'

    def __str__(self):
        return f"{self.name} — {self.service} ({self.submitted_at.date()})"
