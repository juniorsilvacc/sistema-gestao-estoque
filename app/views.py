from django.shortcuts import render
from . import metrics


def custom_500(request, exception=None):
    return render(request, 'errors/_500.html', status=500)

def custom_404(request, exception=None):
    return render(request, 'errors/_404.html', status=404)

def home(request):
    product_metrics = metrics.get_product_metrics()
    sales_metrics = metrics.get_sales_metrics()

    context = {
        'product_metrics': product_metrics,
        'sales_metrics': sales_metrics
    }

    return render(request, 'pages/home.html', context)
