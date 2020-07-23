from django.urls import path,include
from apps.articles import views
urlpatterns = [
    path('', views.ArticlesView.as_view(),name='articles'),
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name='article'),
]
