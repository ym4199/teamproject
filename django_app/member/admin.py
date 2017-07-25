# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from member.forms import MyUserChangeForm, MyUserCreationForm
from member.models import MyUser


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    list_display = ('nickname', 'username', 'email', 'is_admin')
    # admin 페이지에서 관리할 항목들
    list_filter = ('is_admin',)
    fieldsets = (
        ('개인정보', {'fields': ('email', 'username', 'nickname', 'password',)}),
        ('권한', {'fields': ('is_admin',)})
    )

    add_form = MyUserCreationForm
    add_fieldsets = (
        ('기본정보', {'fields': ('email', 'nickname', 'username', 'password1', 'password2',)}),
    )

    search_fields = ('email', 'username', 'nickname',)
    ordering = ('-id',)
    # nickname 으로 정렬
    filter_horizontal = ()


admin.site.register(MyUser, MyUserAdmin)
