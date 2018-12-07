from django.core.exceptions import ValidationError


def content_not_empty(value):
    if value=="":
        raise ValidationError("content must not empty")
