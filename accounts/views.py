from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateResponse

from accounts.models import User
from accounts.forms import UserLoginForm
# Create your views here.

def log_in(request):
	if('username' in request.REQUEST) and ('password' in request.REQUEST):
		username = request.REQUEST['username']
		password = request.REQUEST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/')
		else:
			pass
	return render_to_response('accounts/login.html')

@login_required
def log_out(request):
	logout(request)
	return HttpResponseRedirect('/login/')