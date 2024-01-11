from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'username',
        'email',
        'full_name',
        'phone_number',
        'role',
        'date_of_birth',
        'gender',
        'account_status',
        'registration_date',
        'last_login',
        'is_manager',
        'is_client',
    )

    list_filter = ('account_status', 'is_manager',
                   'is_client', 'gender', 'role')
    search_fields = ('username', 'email', 'full_name')

    readonly_fields = ('registration_date', 'last_login')


# Register the User model with the UserAdmin configuration
admin.site.register(User, UserAdmin)
