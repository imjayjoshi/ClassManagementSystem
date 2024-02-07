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


    #Course
    path('Hod/Course/Add', Hod_views.Add_Course, name='Add_Course'),
    path('Hod/Course/View', Hod_views.View_Course, name='View_Course'),
    path('Hod/Course/Edit/<str:id>', Hod_views.Edit_Course, name='Edit_Course'),
    path('Hod/Course/Update', Hod_views.Update_Course, name='Update_Course'),
    path('Hod/Course/Delete/<str:id>', Hod_views.Delete_Course, name='Delete_Course'),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
