from django.shortcuts import render
from apps.articles import models
# Create your views here.
def home(request):
    context = {}
    queryset = models.Articles.objects.filter(data_status=0)
    context['articles'] = queryset
    return render(request,'pages/home.html',context=context)
