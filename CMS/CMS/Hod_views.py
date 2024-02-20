from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from CMS_APP.models import *
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()

    student_gender_male = Student.objects.filter(gender = 'Male').count()
    student_gender_female = Student.objects.filter(gender = 'Female').count()

    context = {
        'student_count' : student_count,
        'staff_count' : staff_count,
        'course_count' : course_count,
        'subject_count' : subject_count,
        'student_gender_male' : student_gender_male,
        'student_gender_female' : student_gender_female,
    }


    return render(request, 'Hod/home.html' , context)

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

        session = Session_Year.objects.get(id = session_year_id)
        student.session_year_id = session

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

@login_required(login_url='/')
def Update_Staff(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')

        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')


        user = CustomUser.objects.get(id = staff_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != '':
            user.set_password(password)
        if profile_pic != None and profile_pic != '':
            user.profile_pic = profile_pic
        user.save()

        staff = Staff.objects.get(admin = staff_id)
        staff.address = address
        staff.gender = gender

        staff.save()
        messages.success(request, 'Your Profile Updated Successfully !')
        return redirect('View_Staff')
    return render(request, 'Hod/edit_staff.html')

@login_required(login_url='/')
def Delete_Staff(request, admin):
    staff = CustomUser.objects.get(id = admin)
    staff.delete()
    messages.success(request , "Staff deleted Successfully !")
    return redirect('View_Staff')

#Subject CRUD
@login_required(login_url='/')
def Add_Subject(request):
    course = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)

        subject = Subject(
            name = subject_name,
            course = course,
            staff = staff,
        )

        subject.save()
        messages.success(request , "Subject Added Successfully")
        return redirect ('Add_Subject')
    
    context = {
        'course' : course , 
        'staff' : staff ,
    }
    return render(request, 'Hod/add_subject.html' , context)

@login_required(login_url='/')
def View_Subject(request):
    subject = Subject.objects.all()

    context ={
        'subject' : subject,
    }

    return render(request , 'Hod/view_subject.html' , context)


@login_required(login_url='/')
def Edit_Subject(request, id):
    subject = Subject.objects.get(id = id)
    course = Course.objects.all()
    staff = Staff.objects.all()
    
    context ={
        'subject' : subject,
        'course' : course , 
        'staff' : staff ,
    }
    return render(request , 'Hod/edit_subject.html' , context)

@login_required(login_url='/')
def Update_Subject(request):
     if request.method == 'POST':
          subject_id = request.POST.get('subject_id')
          course_id = request.POST.get('course_id')
          staff_id = request.POST.get('staff_id')
          subject_name = request.POST.get('subject_name')
          
          course = Course.objects.get(id = course_id)
          staff = Staff.objects.get(id = staff_id)
          
          subject = Subject(
              id = subject_id,
              name = subject_name,
              course = course,
              staff = staff,            
          )

          subject.save()
          messages.success(request, 'Subject are Successfully Updated')
          
          return redirect('View_Subject')

@login_required(login_url='/')
def Delete_Subject(request, id):
    subject = Subject.objects.get(id = id)
    subject.delete()
    messages.success(request , "Subject deleted Successfully !")
    return redirect('View_Subject')

#Session CRUD
@login_required(login_url='/')
def Add_Session(request):
    if request.method == 'POST':
        session_year_start = request.POST.get('session_start')
        session_year_end = request.POST.get('session_end')

        session = Session_Year(
            session_start = session_year_start,
            session_end = session_year_end,
        )

        session.save()
        messages.success(request, 'Session Are Successfully Created')
        return redirect('Add_Session')
    return render(request , 'Hod/add_session.html')

@login_required(login_url='/')
def View_Session(request):
    session = Session_Year.objects.all()

    context ={
        'session' : session,
    }

    return render(request , 'Hod/view_session.html' , context)


@login_required(login_url='/')
def Edit_Session(request, id):
    session = Session_Year.objects.filter(id = id)

    context = {
        'session' : session,
    }

    return render(request , 'Hod/edit_session.html' , context)
    

@login_required(login_url='/')
def Update_Session(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_start')
        session_year_end = request.POST.get('session_end')

        session = Session_Year(
            id = session_id,
            session_start = session_year_start,
            session_end = session_year_end,
        )
        session.save()
        messages.success(request, 'Session Are Successfully Updated')
        return redirect('View_Session')

@login_required(login_url='/')
def Delete_Session(request, id):
    session = Session_Year.objects.get(id = id)
    session.delete()
    messages.success(request , "Session deleted Successfully !")
    return redirect('View_Session')

@login_required(login_url='/')
def Staff_Send_Noti(request):
    staff = Staff.objects.all()



    context = {
        'staff' : staff
    }
    return render(request, 'Hod/staff_notification.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from CMS_APP.models import *
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()

    student_gender_male = Student.objects.filter(gender = 'Male').count()
    student_gender_female = Student.objects.filter(gender = 'Female').count()

    context = {
        'student_count' : student_count,
        'staff_count' : staff_count,
        'course_count' : course_count,
        'subject_count' : subject_count,
        'student_gender_male' : student_gender_male,
        'student_gender_female' : student_gender_female,
    }


    return render(request, 'Hod/home.html' , context)

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

        session = Session_Year.objects.get(id = session_year_id)
        student.session_year_id = session

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

@login_required(login_url='/')
def Update_Staff(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')

        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')


        user = CustomUser.objects.get(id = staff_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != '':
            user.set_password(password)
        if profile_pic != None and profile_pic != '':
            user.profile_pic = profile_pic
        user.save()

        staff = Staff.objects.get(admin = staff_id)
        staff.address = address
        staff.gender = gender

        staff.save()
        messages.success(request, 'Your Profile Updated Successfully !')
        return redirect('View_Staff')
    return render(request, 'Hod/edit_staff.html')

@login_required(login_url='/')
def Delete_Staff(request, admin):
    staff = CustomUser.objects.get(id = admin)
    staff.delete()
    messages.success(request , "Staff deleted Successfully !")
    return redirect('View_Staff')

#Subject CRUD
@login_required(login_url='/')
def Add_Subject(request):
    course = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)

        subject = Subject(
            name = subject_name,
            course = course,
            staff = staff,
        )

        subject.save()
        messages.success(request , "Subject Added Successfully")
        return redirect ('Add_Subject')
    
    context = {
        'course' : course , 
        'staff' : staff ,
    }
    return render(request, 'Hod/add_subject.html' , context)

@login_required(login_url='/')
def View_Subject(request):
    subject = Subject.objects.all()

    context ={
        'subject' : subject,
    }

    return render(request , 'Hod/view_subject.html' , context)


@login_required(login_url='/')
def Edit_Subject(request, id):
    subject = Subject.objects.get(id = id)
    course = Course.objects.all()
    staff = Staff.objects.all()
    
    context ={
        'subject' : subject,
        'course' : course , 
        'staff' : staff ,
    }
    return render(request , 'Hod/edit_subject.html' , context)

@login_required(login_url='/')
def Update_Subject(request):
     if request.method == 'POST':
          subject_id = request.POST.get('subject_id')
          course_id = request.POST.get('course_id')
          staff_id = request.POST.get('staff_id')
          subject_name = request.POST.get('subject_name')
          
          course = Course.objects.get(id = course_id)
          staff = Staff.objects.get(id = staff_id)
          
          subject = Subject(
              id = subject_id,
              name = subject_name,
              course = course,
              staff = staff,            
          )

          subject.save()
          messages.success(request, 'Subject are Successfully Updated')
          
          return redirect('View_Subject')

@login_required(login_url='/')
def Delete_Subject(request, id):
    subject = Subject.objects.get(id = id)
    subject.delete()
    messages.success(request , "Subject deleted Successfully !")
    return redirect('View_Subject')

#Session CRUD
@login_required(login_url='/')
def Add_Session(request):
    if request.method == 'POST':
        session_year_start = request.POST.get('session_start')
        session_year_end = request.POST.get('session_end')

        session = Session_Year(
            session_start = session_year_start,
            session_end = session_year_end,
        )

        session.save()
        messages.success(request, 'Session Are Successfully Created')
        return redirect('Add_Session')
    return render(request , 'Hod/add_session.html')

@login_required(login_url='/')
def View_Session(request):
    session = Session_Year.objects.all()

    context ={
        'session' : session,
    }

    return render(request , 'Hod/view_session.html' , context)


@login_required(login_url='/')
def Edit_Session(request, id):
    session = Session_Year.objects.filter(id = id)

    context = {
        'session' : session,
    }

    return render(request , 'Hod/edit_session.html' , context)
    

@login_required(login_url='/')
def Update_Session(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_start')
        session_year_end = request.POST.get('session_end')

        session = Session_Year(
            id = session_id,
            session_start = session_year_start,
            session_end = session_year_end,
        )
        session.save()
        messages.success(request, 'Session Are Successfully Updated')
        return redirect('View_Session')

@login_required(login_url='/')
def Delete_Session(request, id):
    session = Session_Year.objects.get(id = id)
    session.delete()
    messages.success(request , "Session deleted Successfully !")
    return redirect('View_Session')

@login_required(login_url='/')
def Staff_Send_Noti(request):
    staff = Staff.objects.all()
    see_notification = Staff_Notification.objects.all()
    
    context = {
        'staff' : staff,
        'see_notification' : see_notification
    }

    return render(request , 'Hod/staff_notification.html' , context)


@login_required(login_url='/')
def Staff_Save_Noti(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(admin = staff_id)
        notification = Staff_Notification(
            staff_id = staff,
            message = message,
        )

        notification.save()
        messages.success(request , "Message Send Successfully !")
        return redirect('Staff_Send_Noti')