import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import metrics


def custom_500(request, exception=None):
    return render(request, 'errors/_500.html', status=500)

def custom_404(request, exception=None):
    return render(request, 'errors/_404.html', status=404)

@login_required(login_url='login')
def home(request):
    product_metrics = metrics.get_product_metrics()
    sales_metrics = metrics.get_sales_metrics()
    daily_sales_data = metrics.get_daily_sales_data()
    daily_sales_quantity_data = metrics.get_daily_sales_quantity_data()
    top_10_stock = metrics.get_top_10_stock_products()
    top_5_sold = metrics.get_top_5_sold_products()

    context = {
        'product_metrics': product_metrics,
        'sales_metrics': sales_metrics,
        'daily_sales_data': json.dumps(daily_sales_data),
        'daily_sales_quantity_data': json.dumps(daily_sales_quantity_data),
        'top_10_stock': json.dumps(top_10_stock),
        'top_5_sold': json.dumps(top_5_sold)
    }

    return render(request, 'pages/home.html', context)
