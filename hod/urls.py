from django.urls import path
from hod.views import home
from hod import views
from django.contrib import admin
urlpatterns = [

 # admin
# path('admin/', admin.site.urls),
path('', home, name='home'), 
path("student_page", views.student_page,name="student_page"),

path("teacher_list", views.teacher_list,name="teacher_list"),
path("add_teacher", views.add_teacher,name="add_teacher"),
path("add_teacher_details", views.add_teacher_details,name="add_teacher_details"),

path("hifz", views.hifz,name="hifz"),
path("addhifz", views.addhifz,name="addhifz"),
path("add_hifz_students", views.add_hifz_students,name="add_hifz_students"),

path("dowra", views.dowra,name="dowra"),
path("adddowra", views.adddowra,name="adddowra"),
path("add_dowra_students", views.add_dowra_students,name="add_dowra_students"),

path("dawa", views.dawa,name="dawa"),
path("adddawa", views.adddawa,name="adddawa"),
path("add_dawa_students", views.add_dawa_students,name="add_dawa_students"),



path("delete_course/<int:id>",views.delete_course,name="delete_course"),
path('course_management/', views.course_management, name='course_management'),
path("add_course_details", views.add_course_details,name="add_course_details"),
path("add_course", views.add_course, name="add_course"),

path("mark_attendance", views.mark_attendance, name="mark_attendance"),
path('mark_student_attendance/', views.mark_student_attendance, name='mark_student_attendance'),
path("view_attendance", views.view_attendance,name="view_attendance"),
    






    
]