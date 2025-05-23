from django.shortcuts import render


def custom_500(request, exception=None):
    return render(request, 'errors/_500.html', status=500)

def custom_404(request, exception=None):
    return render(request, 'errors/_404.html', status=404)

def home(request):
    product_metrics = {
        'total_quantity': 100,
        'total_cost_price': 100000,
        'total_selling_price': 300000,
        'total_profit': 200000
    }

    context = {
        'product_metrics': product_metrics
    }

    return render(request, 'pages/home.html', context)
