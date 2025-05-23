from django.core.management.base import BaseCommand
from faker import Faker
import random

from brands.models import Brand
from categories.models import Category
from suppliers.models import Supplier
from products.models import Product
from inflows.models import Inflow
from outflows.models import Outflow

fake = Faker()

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados de exemplo'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Iniciando a geração de dados...'))

        # Criar Marcas
        for _ in range(20):
            Brand.objects.create(name=fake.company(), description=fake.text())

        # Criar Categorias
        for _ in range(10):
            Category.objects.create(name=fake.word(), description=fake.text())

        # Criar Fornecedores
        for _ in range(15):
            Supplier.objects.create(name=fake.company(), description=fake.text())

        brands = list(Brand.objects.all())
        categories = list(Category.objects.all())
        suppliers = list(Supplier.objects.all())

        # Criar Produtos
        for _ in range(250):
            Product.objects.create(
                title=fake.unique.word(),
                category=random.choice(categories),
                brand=random.choice(brands),
                description=fake.text(),
                serie_number=fake.uuid4(),
                cost_price=round(random.uniform(10, 100), 2),
                selling_price=round(random.uniform(100, 300), 2),
                quantity=random.randint(1, 100)
            )

        products = list(Product.objects.all())

        # Criar Entradas (Inflow)
        for _ in range(100):
            Inflow.objects.create(
                supplier=random.choice(suppliers),
                product=random.choice(products),
                description=fake.text(),
                quantity=random.randint(1, 50)
            )

        # Criar Saídas (Outflow)
        for _ in range(200):
            Outflow.objects.create(
                product=random.choice(products),
                description=fake.text(),
                quantity=random.randint(1, 30)
            )

        self.stdout.write(self.style.SUCCESS('Seed finalizado com sucesso!'))
