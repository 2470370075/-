from django import template
register=template.Library()

@register.filter(name='add')
def add(arg):
    return '{} WJX'.format(arg)

@register.filter(name='add2')
def add2(arg,arg2):
    return '{} {}'.format(arg,arg2)

@register.simple_tag(name='plus')
def f(x,y,z):
    return '{}{}{}'.format(x,y,z)


@register.inclusion_tag('result.html')
def show(n):
    n=1 if n<1 else int(n)
    data=['第{}项'.format(i) for i in range(1,n+1)]
    return {'data':data}

