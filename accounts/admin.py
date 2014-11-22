# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from accounts.models import User
from accounts.forms import UserChangeForm, UserRegistrationForm
# Register your models here.

class UserAdmin(UserAdmin):
	form = UserChangeForm
	add_form = UserRegistrationForm

	list_display = ('username', 'is_admin',)
	list_filter = ('is_admin',)
	fieldsets = (
		(None, {'fields': ('username', 'password',)}),
		('Personal info', {'fields': ('first_name', 'last_name',)}),
		('Permissions', {'fields': ('is_admin',)}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'password1', 'password2',)
		}),
	)
	search_fields = ('username',)
	ordering = ('username',)
	filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)