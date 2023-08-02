from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        category_list = [
            {'name': 'Фрукты', 'description': 'Фрукты из Кавказа'},
            {'name': 'Овощи', 'description': 'Овощи прям с огорода'}
        ]

        categories_for_create = []
        for category in category_list:
            categories_for_create.append(Category(**category))

        print(categories_for_create)

        Category.objects.bulk_create(categories_for_create)

        products_list = [
            {'id': 1, 'name': 'Картошка', 'description': 'Картоха из Беларуссии', 'image': 'картошка.png',
             'category': Category.objects.get(pk=2), 'price': 100},

            {'id': 2, 'name': 'Огурец', 'description': 'Огурцы хрустящие', 'image': 'огурец.png',
             'category': Category.objects.get(pk=2), 'price': 45},

            {'id': 3, 'name': 'Помидор', 'description': 'Самые спелые, красные помидоры', 'image': 'помидор.png',
             'category': Category.objects.get(pk=2), 'price': 45},

            {'id': 4, 'name': 'Банан', 'description': 'Бананы из Африки', 'image': 'банан.png',
             'category': Category.objects.get(pk=1), 'price': 120},

            {'id': 5, 'name': 'Кокос', 'description': 'Только кокосы с высоких пальм', 'image': 'кокос.png',
             'category': Category.objects.get(pk=1), 'price': 155},

            {'id': 6, 'name': 'Яблоко', 'description': 'Яблочки от бабули', 'image': 'яблоко.png',
             'category': Category.objects.get(pk=1), 'price': 99}
        ]

        products_for_create = []
        for product in products_list:
            products_for_create.append(Product(**product))

        print(products_for_create)

        Product.objects.bulk_create(products_for_create)
