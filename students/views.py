from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from .models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'

class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = Student
    fields = ['name', 'roll_number', 'course', 'email', 'date_of_birth']
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')
    success_message = "Student details updated successfully!"

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
