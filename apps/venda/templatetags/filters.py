from django import template


register = template.Library()
def htmlattributes(value, arg):
    attrs = value.field.widget.attrs
    data = arg.replace(' ', '')   
    kvs = data.split(',') 
    for string in kvs:
        kv = string.split(':')
        attrs[kv[0]] = kv[1]
    rendered = str(value)
    return rendered


register = template.Library()
@register.filter
def get_range(value):
  data = value.split('_')
  start = int(data[0])
  end = int(data[1])
  return range(start, end)

register = template.Library()
@register.filter
def inside(value, arg):
    return value in arg

register = template.Library()
@register.filter
def return_item(l, i):
    try:
        return l[i]
    except:
        return None

register.filter('htmlattributes', htmlattributes)
register.filter('get_range', get_range)
register.filter('in', inside)
register.filter('return_item', return_item)
