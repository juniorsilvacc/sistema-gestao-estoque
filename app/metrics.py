from products.models import Product
from outflows.models import Outflow
from django.utils.formats import number_format
from django.db.models import Sum


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