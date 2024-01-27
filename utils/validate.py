from django.core.exceptions import ValidationError

def valideta_png(image):
    name = image.name
    if not name.lower().endswith('.png'):
        raise ValidationError(
            'Somente imagens do tipo png'
        )