# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
	def create_user(self, username, password=None):
		if not username:
			raise ValueError(u'Не задано имя пользователя')
		user = self.model(
			username=username,
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, password):
		user = self.create_user(
			password=password,
			username=username,
		)
		user.is_admin = True
		user.save(using=self._db)
		return user
		

class User(AbstractBaseUser):
	username = models.CharField(u'Имя пользователя', max_length=30, unique=True)
	first_name = models.CharField(u'Имя', max_length=30, blank=True)
	last_name = models.CharField(u'Фамилия', max_length=50, blank=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	class Meta:
		verbose_name_plural="Технологи"
		verbose_name="Технолог"

	USERNAME_FIELD = 'username'
	# REQUIRED_FIELDS = ['username']

	objects = UserManager()

	def get_full_name(self):
		return '%s %s' % (self.first_name, self.last_name,)

	def get_short_name(self):
		return self.username

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.is_admin