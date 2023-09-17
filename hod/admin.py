from django.contrib import admin
from .models import Student,Department,Course,Attendance

# Register your models here.,



admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Course)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'Date', 'Attendance', 'Classes', 'Division')
    list_filter = ('Date', 'Classes', 'Division')
    search_fields = ('student__Student_name', 'Date', 'Classes', 'Division')

