from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from .forms import UserCreationForm,UserChangeForm
from .models import User
# Register your models here.

class UserAdmin(BaseUserAdmin):
    form=UserChangeForm
    add_form=UserCreationForm

    list_display=('email','name','company','userType','jobPosition','phone','is_active','joined','is_admin')
    list_display_links=('company','name','email',)
    list_filter=('userType',)
    fieldsets=(
        (None,{'fields':('email','password')}),
        (_('Personal info'),{'fields':('company','userType','phone','jobPosition')}),
        (_('Permissions'),{'fields':('is_active','is_admin',)}),
    )
    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2','is_staff','is_active','is_admin')
        }),
    )
    search_fields=('email','company','name')
    ordering=('-joined',)
    filter_horizontal=()

admin.site.register(User,UserAdmin)
admin.site.unregister(Group)