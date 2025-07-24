from django import template

register = template.Library()

@register.filter
def format_cnpj(value):
    if value and len(value) == 14:
        return f"{value[:2]}.{value[2:5]}.{value[5:8]}/{value[8:12]}-{value[12:]}"
    return value

@register.filter
def format_cep(value):
    if value and len(value) == 8:
        return f"{value[:5]}-{value[5:]}"
    return value

@register.filter
def format_phone(value):
    if value and len(value) == 10:
        return f"({value[:2]}) {value[2:6]}-{value[6:]}"
    return value

@register.filter
def format_cellphone(value):
    if value and len(value) == 11:
        return f"({value[:2]}) {value[2:7]}-{value[7:]}"
    return value
