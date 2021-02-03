from django import template

register = template.Library()


@register.filter(name='blankrep')
def rep_with_blank(value, arg):
    """"
    This replace "arg" with blank from the string
    """
    return value.replace(arg, '')


#register.filter('blankrep', rep_with_blank)
