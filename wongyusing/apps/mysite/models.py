from django.db import models

# Create your models here.


class MySiteData(models.Model):
    posts = models.IntegerField(verbose_name='文章数', default=0)
    categories = models.IntegerField(verbose_name='分类数', default=0)
    tags = models.IntegerField(verbose_name='标签数', default=0)
    readers = models.IntegerField(verbose_name='读者数', default=0)
    pageviews = models.IntegerField(verbose_name='浏览数', default=0)

    class Meta:
        db_table = 'mysitedata'
        verbose_name = '网站数据'
        verbose_name_plural = verbose_name


class FriendLink(models.Model):
    title = models.CharField(verbose_name='标题', max_length=200)
    link = models.CharField(verbose_name='链接', max_length=200)

    class Meta:
        db_table = 'friendlink'
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class BookLink(models.Model):
    title = models.CharField(verbose_name='标题', max_length=200)
    link = models.CharField(verbose_name='链接', max_length=200)

    class Meta:
        db_table = 'booklink'
        verbose_name = '书籍链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Home(models.Model):
    title = models.CharField(verbose_name='标题', max_length=200)
    desc = models.TextField(verbose_name='簡單描述')

    class Meta:
        db_table = 'home'
        verbose_name = '首页信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(verbose_name='标题', max_length=200)
    desc = models.TextField(verbose_name='簡單描述')

    class Meta:
        db_table = 'about'
        verbose_name = '关于'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
