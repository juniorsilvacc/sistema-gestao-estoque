from django import template

register = template.Library()

@register.filter
def get_translation(translations, key):
    return translations.get(key, key)  # Se não encontrar, mostra o original
