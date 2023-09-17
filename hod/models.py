from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid




class  Login(models.Model):
    Username=models.CharField(max_length=200,null=True)
    Password=models.CharField(max_length=500,null=True)
    Role=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.Username







class Noticeboard(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='hostelmanagment_noticeboard',null=True)    
    Title=models.CharField(max_length=200,null=True)
    Content=models.CharField(max_length=500,null=True)
    Date=models.DateField(null=True)
    Status=models.CharField(max_length=100)

    def __str__(self):
        return self.Title

   


class  Department(models.Model):
    Teacher_name=models.CharField(max_length=200,null=True)
    Contact_no=models.IntegerField(null=True)
    Classes=models.CharField(max_length=100,null=True)
    Department=models.CharField(max_length=100,null=True)           


    def __str__(self):
        return self.Teacher_name




class Hod_registration(models.Model):
    dpt=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hod_registration')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='hostelmanagment_hod_registrations')
    Department_name=models.CharField(max_length=200,null=True)
    Name=models.CharField(max_length=200,null=True)
    Position=models.CharField(max_length=200,null=True)
    Email=models.EmailField(null=True)
    Contact_no=models.IntegerField(null=True)
    Photo=models.ImageField(upload_to='images/')
    Proof=models.ImageField(upload_to='images/')
    Username=models.CharField(max_length=200,null=True)
    Password1=models.CharField(max_length=200,null=True)
    Password2=models.CharField(max_length=200,null=True)
    Status=models.CharField(max_length=100)
    Role=models.CharField(max_length=100)

    def __str__(self):
        return self.Name

    



class  Course(models.Model):
    Course_name=models.CharField(max_length=200,null=True)
    # No_of_students=models.IntegerField(null=True)
    Description=models.CharField(max_length=1000,null=True)
    # Divisions=models.IntegerField(null=True)
    Status=models.CharField(max_length=100)

    def __str__(self):
        return self.Course_name


class Student(models.Model):
    COURSE_CHOICES = (
        ('hifz', 'HIFZ'),
        ('dowra', 'DOWRA'),
        ('dawa', 'DAWA'),
        # Add more course choices if needed
    )
    Admission_no = models.IntegerField(unique=True,null=True)
    Student_name = models.CharField(max_length=100,null=True)
    Address = models.CharField(max_length=100,null=True)
    Place = models.CharField(max_length=100,null=True)
    Post = models.CharField(max_length=100,null=True)
    District = models.CharField(max_length=100,null=True)
    State = models.CharField(max_length=100,null=True)
    Pin_code = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)
    Place_of_birth = models.CharField(max_length=100,null=True)
    Adhar_no = models.IntegerField(null=True)
    Father_name = models.CharField(max_length=100,null=True)
    Father_no = models.IntegerField(unique=True,null=True)
    Father_job = models.CharField(max_length=100,null=True)
    Mother_name = models.CharField(max_length=100,null=True)
    Mother_no = models.IntegerField(unique=True,null=True)
    Mother_job = models.CharField(max_length=100,null=True)
    Guardian_name = models.CharField(max_length=100,null=True)
    Guardian_no = models.IntegerField(unique=True,null=True)
    Guardian_job = models.CharField(max_length=100,null=True)
    Admitted_date = models.DateField(null=True)
    Classes = models.CharField(max_length=100,null=True,choices=COURSE_CHOICES)
    Division = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.Student_name




class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Date = models.DateField()
    Attendance = models.BooleanField(default=False)
    Student_name = models.CharField(max_length=100, null=True)
    Classes = models.CharField(max_length=100, null=True)
    Division = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Student_name





