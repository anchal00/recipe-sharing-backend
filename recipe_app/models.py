from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    posted_by = models.ForeignKey(to='User',
                                on_delete=models.SET_NULL,
                                null=True)
    recipe_body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractUser):
    username_validator = ASCIIUsernameValidator()
    username = models.CharField(
        "Username",
        max_length=50,
        unique=True,
        help_text="Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    first_name = models.CharField("First name", max_length=50, blank=False)
    last_name = models.CharField("Last name", max_length=50, blank=True)
    email = models.EmailField("email address", blank=False, unique=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["username, email, first_name"]
