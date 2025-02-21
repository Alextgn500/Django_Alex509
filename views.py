from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'third_task/home.html')

def products(request):
    games = {
        'Atomic Heart': 'Купить',
        'CyberPunk 2077': 'Купить',
        'PayDay 2': 'Купить',
    }
    return render(request, 'third_task/products.html', {'games': games})

def basket(request):
    return render(request, 'third_task/basket.html')




