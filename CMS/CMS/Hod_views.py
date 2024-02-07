from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from CMS_APP.models import *
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    return render(request, 'Hod/home.html')

# Student CRUD
@login_required(login_url='/')
def Add_Student(request):
    course = Course.objects.all()
    session = Session_Year.objects.all()

    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        if CustomUser.objects.filter(email = email).exists():
            messages.warning(request, "Email is already used")
            return redirect('Add_Student')
        
        if CustomUser.objects.filter(username = username).exists():
            messages.warning(request, "Username is already used")
            return redirect('Add_Student')
        else:
            user  = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3,
                
            )

            user.set_password(password)
            user.save()

            course = Course.objects.get(id = course_id)
            session = Session_Year.objects.get(id = session_year_id)

            student = Student(
                admin = user,
                address = address,
                session_year_id = session,
                course_id = course,
                gender = gender,
            )
            student.save()
            messages.success(request, user.first_name + "  " + user.last_name  + " are successfully saved")
            return redirect('Add_Student')

    context = {
        'course' : course,
        'session' : session,
    }
    return render(request, 'Hod/add_student.html' , context)

@login_required(login_url='/')
def View_Student(request):
    student = Student.objects.all()

    context ={
        'student' : student,
    }

    return render(request, 'Hod/view_student.html' , context)

@login_required(login_url='/')
def Edit_Student(request, id):
    student = Student.objects.filter(id = id)
    course = Course.objects.all()
    session = Session_Year.objects.all()


    context ={
        'student' : student,
        'course' : course,
        'session' : session,
    }

    return render(request, 'Hod/edit_student.html' , context)

@login_required(login_url='/')
def Update_Student(request):
     if request.method == 'POST':
        student_id = request.POST.get('student_id')

        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        user = CustomUser.objects.get(id = student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != '':
            user.set_password(password)
        if profile_pic != None and profile_pic != '':
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin = student_id)
        student.address = address
        student.gender = gender
        course = Course.objects.get(id = course_id)
        student.course_id = course

        sesion = Session_Year.objects.get(id = session_year_id)
        student.session_year_id = sesion

        student.save()
        messages.success(request, 'Your Profile Updated Successfully !')
        return redirect('View_Student')
     return render(request, 'Hod/edit_student.html')

@login_required(login_url='/')
def Delete_Student(request, admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request , "Student deleted Successfully !")
    return redirect('View_Student')

# Course CRUD
@login_required(login_url='/')
def Add_Course(request):
     if request.method == 'POST':
          course_name = request.POST.get('course_name')
          course = Course (
              name = course_name,
          )
          course.save()
          messages.success(request, "Course are Successfully created")
          return redirect('Add_Course')
     return render(request, 'Hod/add_course.html')

@login_required(login_url='/')
def View_Course(request):
    course = Course.objects.all()

    context ={
        'course' : course,
    }

    return render(request, 'Hod/view_course.html' , context)

@login_required(login_url='/')
def Edit_Course(request, id):
    course = Course.objects.get(id = id)

    context ={
        'course' : course,
    }

    return render(request, 'Hod/edit_course.html' , context)

@login_required(login_url='/')
def Update_Course(request):
     if request.method == 'POST':
          name = request.POST.get('name')
          course_id = request.POST.get('course_id')
          
          course = Course.objects.get(id = course_id)
          course.name = name
          
          course.save()
          messages.success(request, "Course are Successfully Updated")
          
          return redirect('View_Course')
     return render(request, 'Hod/edit_course.html')


@login_required(login_url='/')
def Delete_Course(request, id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.success(request , "Course deleted Successfully !")
    return redirect('View_Course')

#Staff CRUD
@login_required(login_url='/')
def Add_Staff(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email = email).exists():
            messages.warning(request, "Email is already taken")
            return redirect('Add_Staff')
        
        if CustomUser.objects.filter(username = username).exists():
            messages.warning(request, "Username is already taken")
            return redirect('Add_Staff')
        
        else:
            user  = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 2,
                
            )
            staff = Staff(
                admin = user,
                address = address,
                gender = gender,
            )

            user.set_password(password)
            user.save()
            staff.save()
            messages.success(request , 'Staff are added Successfully')
    return render(request , 'Hod/add_staff.html')


@login_required(login_url='/')
def View_Staff(request):
    staff = Staff.objects.all()

    context ={
        'staff' : staff,
    }

    return render(request, 'Hod/view_staff.html' , context)

@login_required(login_url='/')
def Edit_Staff(request, id):
    staff = Staff.objects.get(id = id)

    context ={
        'staff' : staff,
    }
    return render(request , 'Hod/edit_staff.html' , context)