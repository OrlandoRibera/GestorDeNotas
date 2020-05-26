from django import template

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    """
        Este template tag está hecho para validar en template los roles de los usuarios (Docente, Alumno)
    """
    return user.groups.filter(name=group_name).exists()
