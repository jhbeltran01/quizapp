from .models import Student
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def credentials_are_incorrect(email):
	email_is_taken = len(Student.objects.filter(email=email)) > 0

	if email_is_taken:
		raise ValidationError(_('The email or password is incorrect'), params={'email': email})