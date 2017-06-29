from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

@csrf_exempt
def user_login(request):#用户登录
	if request.POST:
		username=password=''
		username=request.POST.get('username')
		password=request.POST.get('password')
		user    =authenticate(username=username,password=password)
		if user is not None and user.is_active:
			login(request, user)
			return render(request,'test.html',{'user':user,
												'username':request.user.get_username()})
	ctx={}
	return render(request,'login.html',ctx)	


def success(request):#登录成功提示
    return HttpResponse(request.user.get_username())

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('user_login/')

def diff_response(request):#根据用户是否登录，看到相应的内容
	if request.user.is_authenticated():
		content='<p>my dear user</p>'
	else:
		content='<p>you wired stranger</p>'
	return HttpResponse(content)

@login_required#只能被已登录的用户看到
def user_only(request):
	return HttpResponse("<p>This message is for logged in user only.</p>")

def name_check(user):#指定用户
	return user.get_username()=='daddy'

@user_passes_test(name_check)#只能被指定的用户看到
def specific_user(request):
	return HttpResponse("<p>for daddy only</p>")

def register(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			new_user=form.save()
		return HttpResponseRedirect('/')
	else:
		form=UserCreationForm()
		ctx={'form':form}
		return render(request,'register.html',ctx)		
