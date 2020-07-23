from django.db import models

# Create your models here.


class Keywords(models.Model):
    title = models.CharField(verbose_name='文章关键字',
                             max_length=200, help_text='该关键字用作SEO')

    desc = models.TextField(verbose_name='简介', default='s')


    class Meta:
        db_table = 'keywords'
        verbose_name = '关键字'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ArticleLogo(models.Model):
    title = models.CharField(verbose_name='名称', max_length=40)
    img = models.ImageField(upload_to='article_img', verbose_name='图片')

    class Meta:
        db_table = 'article_logos'
        verbose_name = '图片logo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ArticleTags(models.Model):
    DATASTATUS = (
        (0, '发布'),
        (1, '草稿'),
    )
    data_status = models.IntegerField(
        choices=DATASTATUS, verbose_name='是否发布', default=1)

    title = models.CharField(verbose_name='名称', max_length=40)
    slug = models.SlugField(max_length=30, verbose_name='索引', unique=True)
    keyword = models.ForeignKey(
        Keywords, verbose_name='關鍵字', on_delete=models.CASCADE)
    body = models.TextField(verbose_name='内容')

    class Meta:
        db_table = 'articles_tags'
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title



class ArticleCategory(models.Model):
    DATASTATUS = (
        (0, '发布'),
        (1, '草稿'),
    )
    data_status = models.IntegerField(
        choices=DATASTATUS, verbose_name='是否发布', default=1)
    title = models.CharField(verbose_name='名称', max_length=40)
    slug = models.SlugField(max_length=30, verbose_name='索引', unique=True)
    keyword = models.ForeignKey(
        Keywords, verbose_name='關鍵字', on_delete=models.CASCADE)
    body = models.TextField(verbose_name='内容')

    class Meta:
        db_table = 'article_category'
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Articles(models.Model):
    DATASTATUS = (
        (0, '发布'),
        (1, '草稿'),
    )
    data_status = models.IntegerField(
        choices=DATASTATUS, verbose_name='是否发布', default=1)
    title = models.CharField(verbose_name="标题", max_length=50)
    body = models.TextField(verbose_name="内容")
    author = models.CharField(verbose_name="作者", max_length=50, default='Sing')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    slug = models.SlugField(verbose_name="索引后缀", unique=True)
    script = models.TextField(verbose_name='javascript', default='s')
    keyword = models.ForeignKey(
        Keywords, verbose_name='關鍵字', on_delete=models.CASCADE)
    category = models.ForeignKey(
        ArticleCategory, verbose_name='文章分類', on_delete=models.CASCADE)
    tags = models.ManyToManyField(
        ArticleTags,  verbose_name='文章標籤')
    img = models.ForeignKey(
        ArticleLogo, verbose_name='图片关联', on_delete=models.CASCADE)

    class Meta:
        db_table = 'article'
        verbose_name = '文章'
        verbose_name_plural = '文章列表'
        ordering = ['-created_time']

    # 使对象在后台显示更友善
    def __str__(self):
        return self.title

    def get_pre(self):
        return Articles.objects.filter(id__lt=self.id).order_by('-id').first()

    def get_next(self):
        return Articles.objects.filter(id__gt=self.id).order_by('id').first()
