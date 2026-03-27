from django.contrib import admin
from .models import Product, GalleryPhoto, Service, BookingInquiry


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'currency', 'is_available', 'is_featured']
    list_editable = ['is_available', 'is_featured', 'price']
    list_filter = ['category', 'is_available', 'is_featured']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at']


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ['caption', 'order', 'is_active', 'created_at']
    list_editable = ['order', 'is_active']
    ordering = ['order']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'is_featured']
    list_editable = ['order', 'is_featured']


@admin.register(BookingInquiry)
class BookingInquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'service', 'submitted_at', 'is_read']
    list_editable = ['is_read']
    readonly_fields = ['submitted_at']
    list_filter = ['is_read']
