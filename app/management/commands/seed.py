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
    help = 'Popula o banco de dados com dados reais de eletrônicos'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Iniciando a geração de dados reais...'))

        # Marcas reais
        marcas_reais = [
            "Apple", "Samsung", "Dell", "LG", "Xiaomi",
            "JBL", "Sony", "HyperX", "Acer", "HP",
            "Logitech", "TP-Link", "Redragon", "Amazon", "Kingston",
            "NVIDIA", "Baseus"
        ]
        brands = []
        for nome in marcas_reais:
            brand = Brand.objects.create(name=nome, description=f"Produtos da marca {nome}")
            brands.append(brand)

        # Categorias reais
        categorias_reais = [
            "Smartphones", "Notebooks", "Televisores", "Áudio", "Monitores",
            "Acessórios", "Tablets", "Smartwatches", "Redes", "Armazenamento"
        ]
        categories = []
        for nome in categorias_reais:
            category = Category.objects.create(name=nome, description=f"Categoria de {nome}")
            categories.append(category)

        # Fornecedores genéricos
        fornecedores = []
        for nome in ["Tech Distribuidora", "Mundo Digital", "Importadora TechBrasil", "GigaTech Soluções"]:
            fornecedores.append(Supplier.objects.create(name=nome, description=fake.text()))

        # Produtos reais de eletrônicos
        produtos_reais = [
            ("Smartphone Samsung Galaxy S23", "Smartphones", "Samsung", 2500, 3799),
            ("Notebook Dell Inspiron 15", "Notebooks", "Dell", 2800, 4499),
            ("Televisão LG 50'' 4K UHD", "Televisores", "LG", 2000, 3500),
            ("Console PlayStation 5", "Áudio", "Sony", 3200, 4599),
            ("Fone JBL Tune 510BT", "Áudio", "JBL", 200, 350),
            ("Apple iPad 10ª Geração", "Tablets", "Apple", 3200, 4999),
            ("Monitor Gamer Acer 27''", "Monitores", "Acer", 1200, 2200),
            ("Smartwatch Apple Watch SE", "Smartwatches", "Apple", 1800, 2500),
            ("Notebook Apple MacBook Air M2", "Notebooks", "Apple", 5000, 7999),
            ("Smartphone Xiaomi Redmi Note 13", "Smartphones", "Xiaomi", 1200, 1899),
            ("Headset HyperX Cloud II", "Áudio", "HyperX", 450, 750),
            ("Roteador TP-Link AX3000", "Redes", "TP-Link", 200, 360),
            ("Mouse Logitech MX Master 3S", "Acessórios", "Logitech", 350, 550),
            ("Teclado Mecânico Redragon Kumara", "Acessórios", "Redragon", 250, 399),
            ("Echo Dot 5ª Geração", "Áudio", "Amazon", 300, 450),
            ("SSD Kingston NV2 1TB", "Armazenamento", "Kingston", 300, 500),
            ("Placa de Vídeo NVIDIA RTX 4060", "Acessórios", "NVIDIA", 1600, 2499),
            ("Impressora HP DeskJet 2774", "Acessórios", "HP", 400, 599),
            ("Carregador Turbo Baseus 30W", "Acessórios", "Baseus", 100, 180),
            ("Caixa de Som JBL Charge 5", "Áudio", "JBL", 700, 999),
        ]

        # Criar produtos
        produtos_criados = []
        for nome, categoria_nome, marca_nome, custo, venda in produtos_reais:
            categoria, _ = Category.objects.get_or_create(name=categoria_nome, defaults={"description": f"Categoria de {categoria_nome}"})
            marca, _ = Brand.objects.get_or_create(name=marca_nome, defaults={"description": f"Produtos da marca {marca_nome}"})
            produto = Product.objects.create(
                title=nome,
                category=categoria,
                brand=marca,
                description=fake.text(),
                serie_number=fake.uuid4(),
                cost_price=custo,
                selling_price=venda,
                quantity=random.randint(5, 50)
            )
            produtos_criados.append(produto)

        # Entradas
        for _ in range(50):
            Inflow.objects.create(
                supplier=random.choice(fornecedores),
                product=random.choice(produtos_criados),
                description=fake.text(),
                quantity=random.randint(1, 20)
            )

        # Saídas
        #for _ in range(100):
            #Outflow.objects.create(
                #product=random.choice(produtos_criados),
                #description=fake.text(),
                #quantity=random.randint(1, 10)
            #)

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com dados reais de eletrônicos!'))
