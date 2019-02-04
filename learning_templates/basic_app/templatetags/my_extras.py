from django import template

register = template.Library()

@register.filter(name='cut_that')
def cut_that(value,arg):
    """
    this cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

#register.filter('cut_that',cut_that)
