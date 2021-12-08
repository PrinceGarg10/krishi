from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .forms import registration
from .models import User
from django.contrib import messages
# Create your views here.


#This Fuction Will Add new Item and show All Items
def add_show(request):
    if request.method == 'POST':
        fm = registration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = registration()
            messages.success(request, 'Your details has been submited')
    else:
        fm = registration()
    infor = User.objects.all()
    return render(request, 'krishi/add.html', {'form':fm, 
    'inf':infor})

#this function will update/edit
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk= id)
        fm = registration(request.POST, instance=pi)
        if fm.is_valid:
            fm.save()
            messages.success(request, 'Your details has been updated please Click the Back To Home')

    else:
        pi = User.objects.get(pk= id)
        fm = registration(instance=pi)
    return render(request, 'krishi/update.html', {'form':fm})






#This function will Delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)  
        pi.delete()
        messages.success(request, 'Your details has been successfully deleted..!')
        return HttpResponseRedirect('/')
