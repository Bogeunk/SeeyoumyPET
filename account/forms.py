from django.contrib.auth.models import User
from django.forms import models


class SignupForm(models.forms):
    class Meta:
        model = User