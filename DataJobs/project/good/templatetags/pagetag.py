from django import template
register = template.Library()

#自定义过滤器
@register.filter
def kong_upper(val):
    print('val from template:',val)
    return val.upper()

from django.utils.html import format_html
#自定义标签
@register.simple_tag
def circle_page(curr_page,loop_page):
    offset = abs(curr_page-loop_page)
    if offset < 5:
        if curr_page == loop_page:
            page_ele = '<li class="active"><a href="?page=%s">%s</a></li>'%(loop_page,loop_page)
        else:
            page_ele = '<li><a href="?page=%s">%s</a></li>'%(loop_page,loop_page)
        return format_html(page_ele)
    else:
        return ''