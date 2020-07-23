
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.views import generic

from apps.articles import models


# class HomeView(generic.ListView):
#     model = models.Articles
#     template_name = 'pages/home.html'
#     context_object_name = 'articles'
#     paginate_by = 10
#     paginate_orphans = 2
#
#     def get_queryset(self):
#
#         q1 = Q()
#         q1.connector = 'AND'
#         q1.children.append(('data_status', 0))
#
#         queryset = models.Articles.objects.filter(q1).distinct()
#
#         return queryset


class ArticlesView(generic.ListView):
    model = models.Articles
    template_name = 'pages/article/index.html'
    context_object_name = 'articles'
    paginate_by = 10
    paginate_orphans = 2

    def get_queryset(self):
        category = self.request.GET.get('category', None)
        tags = self.request.GET.getlist('tag', [])
        q1 = Q()
        q1.connector = 'AND'
        q1.children.append(('data_status', 0))
        if category != None:
            category_check = self.check_catagory(category)
            q1.children.append(('category', category_check.id))
        if len(tags) > 0:
            q1 = self.check_tags(tags, q1)

        queryset = models.Articles.objects.filter(q1).distinct()

        return queryset

    def check_catagory(self, slug):
        slug = get_object_or_404(models.ArticleCategory, slug=slug)
        return slug

    def check_tags(self, slugs, q1):
        for each in slugs:
            data = get_object_or_404(models.ArticleTags, slug=each)
            q1.children.append(('tags__id', data.id))

        return q1



class ArticleDetailView(generic.DetailView):
    model = models.Articles
    template_name = 'pages/article/show.html'
    context_object_name = 'articles'
    queryset = models.Articles.objects.filter(data_status=0)
