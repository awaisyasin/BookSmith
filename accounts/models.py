from django.db import models
from django.contrib.auth.models import AbstractUser, User, Group, Permission
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUser(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=200, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="custom_user_set",
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="custom_user_set",
        related_query_name="custom_user",
    )