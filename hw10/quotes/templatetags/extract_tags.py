from django import template

register = template.Library()


def tags(quote_tags):
    return ', '.join([str(quote) for quote in quote_tags.all()])


register.filter('tags', tags)
