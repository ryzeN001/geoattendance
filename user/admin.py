from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import (
    UserAdminCreationForm, 
    UserAdminChangeForm,
)


User = get_user_model()

class UserAdmin(BaseUserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = [
        'ip',
        'user_idnumber',
        'email', 
        'user_lname', 
        'user_fname',
        'admin', 
        'staff', 
        'active',
        'timein',
        'timein_status',
        'timeout',
        'timeout_status',
        'prev_timeout',
        'status'
        ]
    list_filter = [
        'admin', 
        'active', 
        'staff'
        ]
    fieldsets = (
        (None, {'fields': ('user_idnumber','email','password','school', 'user_gender','yearlevel','timein','timein_status', 'timeout', 'timeout_status','present','ip','status')}),
        ('Permissions', {'fields': ('active','admin', 'staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_idnumber', 'password', 'password_confirm', 'email', 'user_lname', 'user_fname', 'user_gender', 'school','yearlevel','admin', 'staff')}
        ),
    )

    search_fields = [
        'email', 
        'user_fname'
        ]
    ordering = ['email']
    filter_horizontal = (
        'user_permissions', 
        'groups'
        )


admin.site.register(User, UserAdmin)
admin.site.site_header = "GeoAttendance Admin"