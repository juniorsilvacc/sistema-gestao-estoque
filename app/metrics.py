from products.models import Product
from outflows.models import Outflow
from django.utils.formats import number_format
from django.db.models import Sum
from datetime import timedelta
from django.utils import timezone


def get_product_metrics():
    products = Product.objects.all()

    quantity_product = sum(product.quantity for product in products)
    total_cost_price = sum(product.cost_price * product.quantity for product in products)
    total_selling_price = sum(product.selling_price * product.quantity for product in products)
    total_profit = total_selling_price - total_cost_price
 
    product_metrics = {
        'quantity_product': quantity_product,
        'total_cost_price': number_format(total_cost_price, decimal_pos=2, force_grouping=True),
        'total_selling_price': number_format(total_selling_price, decimal_pos=2, force_grouping=True),
        'total_profit': number_format(total_profit, decimal_pos=2, force_grouping=True),
    }

    return product_metrics


def get_sales_metrics():
    outflows = Outflow.objects.all()

    quantity_sales = Outflow.objects.count()
    product_sales = Outflow.objects.aggregate(total=Sum('quantity'))['total'] or 0
    total_sales_value = sum(outflow.quantity * outflow.product.selling_price for outflow in outflows)
    total_sales_cost_price = sum(outflow.quantity * outflow.product.cost_price for outflow in outflows)
    total_sales_profit = total_sales_value - total_sales_cost_price

    sales_metrics = {
        'quantity_sales': quantity_sales,
        'product_sales': product_sales,
        'total_sales_value': number_format(total_sales_value, decimal_pos=2, force_grouping=True),
        'total_sales_profit': number_format(total_sales_profit, decimal_pos=2, force_grouping=True),
    }

    return sales_metrics


def get_last_7_days():
    today = timezone.now().date()
    return [today - timedelta(days=i) for i in range(6, -1, -1)]

def get_daily_sales_data():
    """
    Total monetário diário de saídas (considerando preço de venda do produto * quantidade).
    """
    from products.models import Product

    dates = get_last_7_days()
    labels = []
    values = []

    for day in dates:
        outflows = Outflow.objects.filter(created_at__date=day)
        total = 0

        for outflow in outflows.select_related('product'):
            total += outflow.quantity * outflow.product.selling_price

        labels.append(day.strftime('%d/%m'))
        values.append(float(total))

    return {
        'dates': labels,
        'values': values
    }

def get_daily_sales_quantity_data():
    """
    Quantidade total de produtos que saíram por dia.
    """
    dates = get_last_7_days()
    labels = []
    quantities = []

    for day in dates:
        quantity = Outflow.objects.filter(created_at__date=day).aggregate(Sum('quantity'))['quantity__sum'] or 0
        labels.append(day.strftime('%d/%m'))
        quantities.append(quantity)

    return {
        'dates': labels,
        'values': quantities
    }


def get_top_10_stock_products():
    """
    Estoque Atual por Produto (Top 10)
    """
    top_products = Product.objects.order_by('-quantity')[:10]
    return {
        'labels': [p.title for p in top_products],
        'data': [p.quantity for p in top_products],
    }


def get_top_5_sold_products():
    """
    Top 5 Produtos Mais Vendidos
    """
    top_sold = (
        Outflow.objects.values('product__title')
        .annotate(total_sold=Sum('quantity'))
        .order_by('-total_sold')[:5]
    )
    return {
        'labels': [item['product__title'] for item in top_sold],
        'data': [item['total_sold'] for item in top_sold],
    }