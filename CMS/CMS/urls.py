from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views, Hod_views, Staff_views, Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('', views.Login, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    # profile update
    path('profile', views.profile, name='profile'),
    path('profile/update', views.profile_update, name='profile_update'),
    path('doLogout', views.doLogout, name='logout'),


    # HOD panel
    # Student
    path('Hod/Home', Hod_views.HOME, name='hod_home'),
    path('Hod/Student/Add', Hod_views.Add_Student, name='Add_Student'),
    path('Hod/Student/View', Hod_views.View_Student, name='View_Student'),
    path('Hod/Student/Edit/<str:id>', Hod_views.Edit_Student, name='Edit_Student'),
    path('Hod/Student/Update', Hod_views.Update_Student, name='Update_Student'),
    path('Hod/Student/Delete/<str:admin>', Hod_views.Delete_Student, name='Delete_Student'),

    # Staff
    path('Hod/Staff/Add', Hod_views.Add_Staff, name='Add_Staff'),
    path('Hod/Staff/View', Hod_views.View_Staff, name='View_Staff'),
    path('Hod/Staff/Edit/<str:id>', Hod_views.Edit_Staff, name='Edit_Staff'),
    path('Hod/Staff/Update', Hod_views.Update_Staff, name='Update_Staff'),
    path('Hod/Staff/Delete/<str:admin>', Hod_views.Delete_Staff, name='Delete_Staff'),

    #Course
    path('Hod/Course/Add', Hod_views.Add_Course, name='Add_Course'),
    path('Hod/Course/View', Hod_views.View_Course, name='View_Course'),
    path('Hod/Course/Edit/<str:id>', Hod_views.Edit_Course, name='Edit_Course'),
    path('Hod/Course/Update', Hod_views.Update_Course, name='Update_Course'),
    path('Hod/Course/Delete/<str:id>', Hod_views.Delete_Course, name='Delete_Course'),

    #Subject
    path('Hod/Subject/Add', Hod_views.Add_Subject, name='Add_Subject'),
    path('Hod/Subject/View', Hod_views.View_Subject, name='View_Subject'),
    path('Hod/Subject/Edit/<str:id>', Hod_views.Edit_Subject, name='Edit_Subject'),
    path('Hod/Subject/Update', Hod_views.Update_Subject, name='Update_Subject'),
    path('Hod/Subject/Delete/<str:id>', Hod_views.Delete_Subject, name='Delete_Subject'),

    #Session
    path('Hod/Session/Add', Hod_views.Add_Session, name='Add_Session'),
    path('Hod/Session/View', Hod_views.View_Session, name='View_Session'),
    path('Hod/Session/Edit/<str:id>', Hod_views.Edit_Session, name='Edit_Session'),
    path('Hod/Session/Update', Hod_views.Update_Session, name='Update_Session'),
    path('Hod/Session/Delete/<str:id>', Hod_views.Delete_Session, name='Delete_Session'),


    #Notification
    path('Hod/Staff/Send_Notification', Hod_views.Staff_Send_Noti, name='Staff_Send_Noti'),
    path('Hod/Staff/Save_Notification', Hod_views.Staff_Save_Noti, name='Staff_Save_Noti'),

    # STAFF panel
    path('Staff/Home', Staff_views.HOME, name='staff_home'),
    path('Staff/Notification', Staff_views.Notification, name='Notification'),
    path('Staff/mark_as_read/<str:status>', Staff_views.mark_as_read, name='mark_as_read'),
    path('Staff/Apply_Leave', Staff_views.Apply_Leave, name='Apply_Leave'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
