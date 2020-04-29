from django import template
import datetime as dt
register=template.Library()
@register.simple_tag(name="get_date")

def get_date():
    now=dt.datetime.now()
    return now
@register.filter
def quotes(value):
    s='"'+str(value)+'"'
    return s
