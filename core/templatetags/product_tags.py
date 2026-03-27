from django import template
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def product_image_url(product):
    """Return the product image URL, falling back to static files for Vercel."""
    if product.image and product.image.name:
        filename = product.image.name.split('/')[-1]
        # Always serve from static on Vercel (media is read-only)
        # This also works locally since we have copies in both places
        return static(f'img/products/{filename}')
    return static('img/products/placeholder.jpeg')
