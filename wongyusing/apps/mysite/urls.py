
from django.urls import path,include
from apps.mysite import views
urlpatterns = [
    path('', views.home,name='home'),
]
