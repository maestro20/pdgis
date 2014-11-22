# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from accounts.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserRegistrationForm(forms.ModelForm):
	password1 = forms.CharField(label=u'Пароль', widget=forms.PasswordInput)
	password2 = forms.CharField(label=u'Подтверждение пароля', widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ('username',)

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Пароли не совпадают!")
		return password2

	def save(self, commit=True):
		user = super(UserRegistrationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user


class UserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = User
		fields = ('password',)

	def clean_password(self):
		return self.initial['password']


class UserLoginForm(forms.Form):
	username = forms.CharField(label = u'Имя пользователя', max_length=20)
	password = forms.CharField(label = u'Пароль', widget=forms.PasswordInput)