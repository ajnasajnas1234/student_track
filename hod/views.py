from django.shortcuts import get_object_or_404,render,redirect
from . import models
from django.contrib.auth.models import User
from .models import Student,Department,Course,Attendance
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
from .forms import AttendanceForm

# admin


def home(request):
    return render(request, 'admins/home.html')

def student_page(request):
    data=Student.objects.all()
    return render(request,'admins/student_page.html',{'data':data})

def teacher_list(request):
    teachers = Department.objects.all()  # Query all teacher records from the database
    return render(request, 'admins/teachers.html', {'teachers': teachers})
    
def add_teacher(request):
    data=Department.objects.all()
    return render(request,'admins/add_teacher.html',{'data':data})

def add_course_details(request):
    data = Course.objects.all()  # Query all teacher records from the database
    return render(request, 'admins/addcourse.html', {'data': data})

def hifz(request):
    data = Student.objects.filter(Classes='hifz')
    return render(request, 'admins/hifz.html', {'students': data})

def addhifz(request):
    data = Student.objects.all()
    return render(request, 'admins/addhifz.html', {'students': data})


def dowra(request):
    data = Student.objects.filter(Classes='dowra')
    return render(request, 'admins/dowra.html', {'students': data})

def adddowra(request):
    data = Student.objects.all()
    return render(request, 'admins/adddowra.html', {'students': data})


def dawa(request):
    data = Student.objects.filter(Classes='dawa')
    return render(request,'admins/dawa.html', {'students': data})

def adddawa(request):
    data = Student.objects.all()
    return render(request, 'admins/adddawa.html', {'students': data})



def course_management(request):
    data = Course.objects.all()  # Fetch all courses from the database
    return render(request, 'admins/courses.html', {'data': data})

def view_attendance(request):
    data = Attendance.objects.all()
    return render(request,'admins/viewattendance.html',{'data' : data})


def add_teacher_details(request):
    if request.method == 'POST':
        teacher_name = request.POST.get('teacher_name')
        contact = request.POST.get('contact')
        classes = request.POST.get('classes')
        department = request.POST.get('department')
        status = "0"

        # Create and save a new Department object
        new_teacher = Department(
            Teacher_name=teacher_name,
            Contact_no=contact,
            Classes=classes,
            Department=department
        )
        new_teacher.save()

        # Redirect to the teacher list page after adding a teacher
        return redirect('teacher_list')
    else:
        # Retrieve the list of all teachers from the database
        teachers = Department.objects.all()

        # Pass the list of teachers to the template
        return render(request, 'admins/teachers.html', {'students': teachers})



def add_hifz_students(request):
    if request.method == 'POST':
        admission = request.POST.get('admission')
        stud = request.POST.get('stud')
        address = request.POST.get('address')
        place = request.POST.get('place')
        dist = request.POST.get('dist')
        post = request.POST.get('post')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        dob = request.POST.get('dob')
        placebirth = request.POST.get('placebirth')
        adhar = request.POST.get('adhar')
        father = request.POST.get('father')
        fatherno = request.POST.get('fatherno')
        fatherjob = request.POST.get('fatherjob')
        mother = request.POST.get('mother')
        motherno = request.POST.get('motherno')
        motherjob = request.POST.get('motherjob')
        guardian = request.POST.get('guardian')
        guardianno = request.POST.get('guardianno')
        guardianjob = request.POST.get('guardianjob')
        dateadmission = request.POST.get('dateadmission')
        classes = request.POST.get('class')
        division = request.POST.get('division')
        
        status = "0"

        # Create and save a new Department object
        new_student = Student(
            Admission_no=admission,
            Student_name=stud,
            Address=address,
            Place=place,
            Post=post,
            District=dist,
            State=state,
            Pin_code=pin,
            date_of_birth=dob,
            Place_of_birth=placebirth,
            Adhar_no=adhar,
            Father_name=father,
            Father_no=fatherno,
            Father_job=fatherjob,
            Mother_name=mother,
            Mother_no=motherno,
            Mother_job=motherjob,
            Guardian_name=guardian,
            Guardian_no=guardianno,
            Guardian_job=guardianjob,
            Admitted_date=dateadmission,
            Classes=classes,
            Division=division
        
        )
        new_student.save()

        # Redirect to the teacher list page after adding a teacher
        return redirect('hifz')
    else:
        # Retrieve the list of all teachers from the database
        students = Student.objects.filter(Classes='hifz')

        # Pass the list of teachers to the template
        return render(request, 'admins/hifz.html', {'students': students})




def add_dowra_students(request):
    if request.method == 'POST':
        admission = request.POST.get('admission')
        stud = request.POST.get('stud')
        address = request.POST.get('address')
        place = request.POST.get('place')
        dist = request.POST.get('dist')
        post = request.POST.get('post')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        dob = request.POST.get('dob')
        placebirth = request.POST.get('placebirth')
        adhar = request.POST.get('adhar')
        father = request.POST.get('father')
        fatherno = request.POST.get('fatherno')
        fatherjob = request.POST.get('fatherjob')
        mother = request.POST.get('mother')
        motherno = request.POST.get('motherno')
        motherjob = request.POST.get('motherjob')
        guardian = request.POST.get('guardian')
        guardianno = request.POST.get('guardianno')
        guardianjob = request.POST.get('guardianjob')
        dateadmission = request.POST.get('dateadmission')
        classes = request.POST.get('class')
        division = request.POST.get('division')
        
        status = "0"

        # Create and save a new Department object
        new_student = Student(
            Admission_no=admission,
            Student_name=stud,
            Address=address,
            Place=place,
            Post=post,
            District=dist,
            State=state,
            Pin_code=pin,
            date_of_birth=dob,
            Place_of_birth=placebirth,
            Adhar_no=adhar,
            Father_name=father,
            Father_no=fatherno,
            Father_job=fatherjob,
            Mother_name=mother,
            Mother_no=motherno,
            Mother_job=motherjob,
            Guardian_name=guardian,
            Guardian_no=guardianno,
            Guardian_job=guardianjob,
            Admitted_date=dateadmission,
            Classes=classes,
            Division=division
        
        )
        new_student.save()

        # Redirect to the teacher list page after adding a teacher
        return redirect('dowra')
    else:
        # Retrieve the list of all teachers from the database
        students = Student.objects.filter(Classes='dowra')

        # Pass the list of teachers to the template
        return render(request, 'admins/dowra.html', {'students': students})




        
def add_dawa_students(request):
    if request.method == 'POST':
        admission = request.POST.get('admission')
        stud = request.POST.get('stud')
        address = request.POST.get('address')
        place = request.POST.get('place')
        dist = request.POST.get('dist')
        post = request.POST.get('post')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        dob = request.POST.get('dob')
        placebirth = request.POST.get('placebirth')
        adhar = request.POST.get('adhar')
        father = request.POST.get('father')
        fatherno = request.POST.get('fatherno')
        fatherjob = request.POST.get('fatherjob')
        mother = request.POST.get('mother')
        motherno = request.POST.get('motherno')
        motherjob = request.POST.get('motherjob')
        guardian = request.POST.get('guardian')
        guardianno = request.POST.get('guardianno')
        guardianjob = request.POST.get('guardianjob')
        dateadmission = request.POST.get('dateadmission')
        classes = request.POST.get('class')
        division = request.POST.get('division')
        
        status = "0"

        # Create and save a new Department object
        new_student = Student(
            Admission_no=admission,
            Student_name=stud,
            Address=address,
            Place=place,
            Post=post,
            District=dist,
            State=state,
            Pin_code=pin,
            date_of_birth=dob,
            Place_of_birth=placebirth,
            Adhar_no=adhar,
            Father_name=father,
            Father_no=fatherno,
            Father_job=fatherjob,
            Mother_name=mother,
            Mother_no=motherno,
            Mother_job=motherjob,
            Guardian_name=guardian,
            Guardian_no=guardianno,
            Guardian_job=guardianjob,
            Admitted_date=dateadmission,
            Classes=classes,
            Division=division
        
        )
        new_student.save()

        # Redirect to the teacher list page after adding a teacher
        return redirect('dawa')
    else:
        # Retrieve the list of all teachers from the database
        students = Student.objects.filter(Classes='dawa')

        # Pass the list of teachers to the template
        return render(request, 'admins/dawa.html', {'students': students})



def add_course(request):
    if request.method == 'POST':
        course = request.POST.get('course')
        description = request.POST.get('description')
        status = "0"

        detail = Course(Course_name=course, Description=description)  # Use the Course model
        detail.save()  # Save the new course to the database

        print('Course added successfully')
        return redirect('course_management')
    else:
        # Retrieve the list of all courses from the database
        data = Course.objects.all()

        # Pass the list of courses to the template
        return render(request, 'admins/courses.html', {'data': data})


def delete_course(request, id):
    delmember = Course.objects.get(id=id)
    print(delmember)
    delmember.delete()
    return redirect('course_management')

def mark_attendance(request):
    data = Student.objects.all()
    return render(request, 'admins/markattendance.html', {'data': data})

def mark_student_attendance(request):
    students = Student.objects.all()
    
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            for student in students:
                field_name = f'student_{student.id}'
                attendance_status = request.POST.get(field_name, False) == 'on'
                Attendance.objects.create(
                    student=student,
                    Date=date,
                    Attendance=attendance_status,
                    Student_name=student.Student_name,
                    Classes=student.Classes,
                    Division=student.Division
                )
            return redirect('mark_attendance')  # Redirect after successfully marking attendance
    else:
        form = AttendanceForm()
    
    context = {
        'students': students,
        'form': form,
    }
    
    return render(request, 'admins/markattendance.html', context)



# def mark_attendance_page(request):
    
#     attendance_records = Attendance.objects.all()
    
   
#     students = Student.objects.all()
    
#     return render(request, 'student.html', {'attendance_records': attendance_records, 'students': students})




# def mark_student_attendance(request):
#     if request.method == 'POST':
#         month = int(request.POST.get('month'))
#         course = request.POST.get('course')
#         student_name = request.POST.get('student')
#         division = request.POST.get('division')

#         # Get the current date
#         current_date = datetime.now().date()

#         # Get the student ID based on the student's name
#         try:
#             student = Student.objects.get(Student_name=student_name, Classes=course, Division=division)
#         except Student.DoesNotExist:
#             messages.error(request, 'Student with the provided name not found in the selected course and division.')
#             return redirect('mark_student_attendance')

#         # Check if attendance already exists for the given student, month, and course
#         existing_attendance = Attendance.objects.filter(
#             st=student,
#             Date=current_date,
#             Month=month,
#             Course_name=course,
#             Division=division
#         )

#         if existing_attendance.exists():
#             messages.error(request, 'Attendance already marked for this student in the selected month and course.')
#         else:
#             # Create and save the new attendance record
#             attendance = Attendance(
#                 st=student,
#                 Date=current_date,
#                 Month=month,
#                 Course_name=course,
#                 Division=division,
#                 status='Present'  # You can change this based on your form data
#             )
#             attendance.save()
#             messages.success(request, 'Attendance marked successfully.')

#     # Render the page with form
#     students = Student.objects.filter(Classes=course, Division=division)
#     return render(request, 'mark_attendance.html', {'students': students})



    


