from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'course', 'email', 'date_of_birth')
    search_fields = ('name', 'roll_number', 'email')
    list_filter = ('course',)

