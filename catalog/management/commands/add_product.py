from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        category_list = [
            {'id': 3, 'name': 'Ягоды', 'description': 'Самые вкусные ягодки для твоего торта'}
        ]

        categories_for_create = []
        for category in category_list:
            categories_for_create.append(Category(**category))

        Category.objects.bulk_create(categories_for_create)

        products_list = [
            {'name': 'Авокадо', 'description': 'Для бутерброда с яичками — самое то!', 'image': 'авокадо.png',
             'category': Category.objects.get(pk=3), 'price': 222}
        ]

        products_for_create = []
        for product in products_list:
            products_for_create.append(Product(**product))

        print(products_for_create)

        Product.objects.bulk_create(products_for_create)
