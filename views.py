from django.views import View
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'second_task/func_template.html')

class ClassTemplateView(View):
    def get(self, request):
        return render(request, 'second_task/class_template.html')


