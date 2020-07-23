from django import template
from apps.mysite import models
register = template.Library()



@register.simple_tag
def site_data():
    return models.MySiteData.objects.all()[0]
