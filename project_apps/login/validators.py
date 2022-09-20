from .models import Student
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def credentials_are_incorrect(email):
	raise ValidationError(_('The email or password is incorrect'), params={'email': email})