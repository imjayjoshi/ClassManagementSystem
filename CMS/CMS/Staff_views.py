from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from CMS_APP.models import *
from django.contrib import messages

@login_required(login_url='/')
def HOME(request):
    return render(request, 'Staff/home.html')

@login_required(login_url='/')
def Notification(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id

        notification = Staff_Notification.objects.filter(staff_id = staff_id)

        context = {
            'notification' : notification,
        }
    return render(request , 'Staff/notification.html', context)

@login_required(login_url='/')
def mark_as_read(request, status):
    notification = Staff_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()

    return redirect('Notification')

@login_required(login_url='/')
def Apply_Leave(request):
    
    return render(request , 'Staff/apply_leave.html')