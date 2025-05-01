from django import template
from ..models import MenuItem
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(name=menu_name).select_related('parent')
    return mark_safe(render_menu(menu_items))

def render_menu(menu_items):
    menu_html = '<ul class="hover">'
    for item in menu_items:
        menu_html += '<li>'
        if item.url:
            menu_html += f'<a href="{item.url}">{item.name}</a>'
        else:
            menu_html += item.name
        if item.children.exists():
            menu_html += render_menu(item.children.all())
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html
