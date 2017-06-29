from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from west.models import Character
from django.views.decorators.csrf import csrf_exempt
from django import forms

def first_page(request):
    return HttpResponse("西餐")
def staff(request):
	staff_list=Character.objects.all()
	staff_str=map(str,staff_list)
	return HttpResponse(""+' '.join(staff_str)+' ')
def templay(request):
	staff_list   = Character.objects.all()
	# staff_str   = map(str,staff_list)
	# context   = {'label':' '.join(staff_str)}
	return render(request, 'templay.html',{'staffs':staff_list})
def form(request):
	return render(request,'form.html')

class CharacterForm(forms.Form):
	name=forms.CharField(max_length=200)
	
@csrf_exempt
def investigate(request):
	if request.POST:
		form=CharacterForm(request.POST)
		if form.is_valid():
			submitted=form.cleaned_data['name']
			new_record=Character(name=submitted)
			new_record.save()
	form=CharacterForm()
	ctx={}
	all_records=Character.objects.all()
	ctx['staff']=all_records
	ctx['form']=form	
	return render(request,'investigate.html',ctx)
	