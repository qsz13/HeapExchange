from django import template

register = template.Library()

@register.filter
def post_href(value):
    type = value.__class__.__name__
    type = type.lower()
    link = r'\"{%% url \'' + type + r'_detail\' post.id %%}\"'
    #link = link.encode("UTF-8") 
    return unicode(link)