from django.core.management.base import BaseCommand
from django.conf import settings
from core.models import Service, Product


class Command(BaseCommand):
    help = 'Seed services and products with real images'

    def handle(self, *args, **kwargs):
        # Services
        services_data = [
            {'name': 'Press-On Nails', 'description': 'Ready-made nail sets in stunning designs. Pick your style, apply at home, and slay all day. Ships worldwide.', 'icon': '\U0001f485', 'cta_text': 'Shop Now', 'is_featured': True, 'order': 1},
            {'name': 'Custom Nail Sets', 'description': 'Your vision, our craft. Tell Thelma your dream design and get a one-of-a-kind set made just for you.', 'icon': '\u2728', 'cta_text': 'Order Custom', 'is_featured': True, 'order': 2},
            {'name': 'Nail Application', 'description': 'In-person nail application service in Buea. Professional, clean, and flawless every time.', 'icon': '\U0001f3a8', 'cta_text': 'Book Now', 'is_featured': True, 'order': 3},
        ]
        for s in services_data:
            obj, created = Service.objects.get_or_create(name=s['name'], defaults=s)
            if not created:
                for key, val in s.items():
                    setattr(obj, key, val)
                obj.save()

        # Products with images
        products_data = [
            {'name': 'Pink Leopard Set', 'image_file': 'pink-leopard-set.jpeg', 'description': 'Soft pink press-ons with chic leopard print accents at the base. Sweet meets fierce in this bestselling set.', 'price': 5000, 'category': 'press_on', 'is_featured': True, 'is_available': True, 'duration': '2-3 weeks', 'best_for': 'Daily wear, brunch dates'},
            {'name': 'Cherry Valentine', 'image_file': 'cherry-valentine.jpeg', 'description': 'Deep cherry red stilettos mixed with pink French tips and heart-shaped accents. Love in every detail.', 'price': 7000, 'category': 'press_on', 'is_featured': True, 'is_available': True, 'duration': '2-3 weeks', 'best_for': 'Valentines, date nights'},
            {'name': 'Cherry Valentine Duo', 'image_file': 'cherry-valentine-duo.jpeg', 'description': 'The ultimate duo — deep cherry square nails paired with cherry-pink stilettos. Two looks, one package.', 'price': 12000, 'category': 'press_on', 'is_featured': True, 'is_available': True, 'duration': '2-3 weeks', 'best_for': 'Gift sets, mix & match'},
            {'name': 'Red Floral Glam', 'image_file': 'red-floral-glam.jpeg', 'description': 'Nude and red stiletto set with hand-crafted 3D flower accents and chrome details. Passionate and bold.', 'price': 8000, 'category': 'custom', 'is_featured': True, 'is_available': True, 'duration': '2-3 weeks', 'best_for': 'Events, photo shoots'},
            {'name': 'Celestial Frost', 'image_file': 'celestial-frost.jpeg', 'description': 'Nude pink stilettos with icy blue marble swirls, gold star charms, and crystal accents. Dreamy and ethereal.', 'price': 9000, 'category': 'custom', 'is_featured': True, 'is_available': True, 'duration': '2-3 weeks', 'best_for': 'Winter events, holidays'},
            {'name': 'Autumn Floral Stiletto', 'image_file': 'autumn-floral-stiletto.jpeg', 'description': 'Warm brown and orange stiletto set with hand-painted floral nail art and crystal detail. Cozy and chic.', 'price': 7000, 'category': 'press_on', 'is_featured': True, 'is_available': True, 'duration': '2-3 weeks', 'best_for': 'Autumn, daily wear'},
            {'name': 'Bridal Elegance', 'image_file': 'bridal-elegance.jpeg', 'description': 'Soft nude stilettos with gold chrome accents, delicate 3D florals, and pearl details. The perfect bridal set.', 'price': 15000, 'category': 'custom', 'is_featured': True, 'is_available': True, 'duration': '3-4 weeks', 'best_for': 'Weddings, engagements'},
            {'name': 'Orange Luxe Leopard', 'image_file': 'orange-luxe-leopard.jpeg', 'description': 'Vibrant orange stilettos with leopard print accent nail and gold charm details. Fierce and unforgettable.', 'price': 7000, 'category': 'press_on', 'is_featured': True, 'is_available': True, 'duration': '2-3 weeks', 'best_for': 'Parties, bold looks'},
            {'name': 'Floral Garden', 'image_file': 'floral-garden.jpeg', 'description': 'Nude almond nails adorned with hand-crafted 3D flowers in purple, pink, and yellow. Wearable art.', 'price': 9000, 'category': 'custom', 'is_featured': True, 'is_available': True, 'duration': '2-3 weeks', 'best_for': 'Spring, romantic occasions'},
            {'name': 'Classic Pink French', 'image_file': 'classic-pink-french.jpeg', 'description': 'Timeless pink and white stiletto set with crystal flower accent. Simple, elegant, always in style.', 'price': 5000, 'category': 'press_on', 'is_featured': True, 'is_available': True, 'duration': '2-3 weeks', 'best_for': 'Everyday, office'},
            {'name': 'Ruby Glam', 'image_file': 'ruby-glam.jpeg', 'description': 'Deep metallic red stiletto nails with a mirror-like glitter finish. Bold, luxurious, and head-turning.', 'price': 6000, 'category': 'press_on', 'is_featured': True, 'is_available': True, 'duration': '2-3 weeks', 'best_for': 'Nights out, events'},
            {'name': 'Pink Noir', 'image_file': 'pink-noir.jpeg', 'description': 'Pink and black stiletto set with drip art design. Where edgy meets feminine for a statement look.', 'price': 7000, 'category': 'custom', 'is_featured': True, 'is_available': True, 'duration': '2-3 weeks', 'best_for': 'Parties, concerts'},
            {'name': 'Peach Blossom Chrome', 'image_file': 'peach-blossom-chrome.jpeg', 'description': 'Soft peach nails with gold chrome drip details and 3D flower accent. Modern elegance at its finest.', 'price': 8000, 'category': 'custom', 'is_featured': True, 'is_available': True, 'duration': '2-3 weeks', 'best_for': 'Bridal showers, events'},
            {'name': 'Golden Sunset Stiletto', 'image_file': 'golden-sunset-stiletto.jpeg', 'description': 'Warm nude and orange gradient stilettos with leaf and floral accents. Inspired by Cameroon sunsets.', 'price': 7000, 'category': 'press_on', 'is_featured': True, 'is_available': True, 'duration': '2-3 weeks', 'best_for': 'Summer, special occasions'},
            {'name': 'Butterfly Wings', 'image_file': 'butterfly-wings.jpeg', 'description': 'Nude French tip base with hand-painted butterfly wing art in vibrant orange, green, and blue. Wearable art.', 'price': 8000, 'category': 'custom', 'is_featured': True, 'is_available': True, 'duration': '2-3 weeks', 'best_for': 'Festivals, photo shoots'},
            {'name': 'Tropical Mix', 'image_file': 'tropical-mix.jpeg', 'description': 'Bold mix of mauve, orange, floral and leopard details. For the woman who wants all the vibes in one set.', 'price': 7000, 'category': 'custom', 'is_featured': True, 'is_available': True, 'duration': '2-3 weeks', 'best_for': 'Festivals, summer'},
        ]

        media_src = settings.MEDIA_ROOT / 'products'
        for p in products_data:
            image_file = p.pop('image_file')
            image_path = media_src / image_file

            obj, created = Product.objects.get_or_create(name=p['name'], defaults=p)
            if not created:
                for key, val in p.items():
                    if key != 'name':
                        setattr(obj, key, val)

            # Assign image if file exists and product doesn't have one yet or needs update
            if image_path.exists():
                obj.image.name = f'products/{image_file}'
                obj.save()

        self.stdout.write(self.style.SUCCESS(f'Seeded {len(services_data)} services and {len(products_data)} products with images.'))
