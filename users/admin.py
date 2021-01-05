from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    # list_display = ("username", "gender", "language", "currency", "superhost")
    # list_filter = ("superhost", "language", "currency")
