from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import generic
from .forms import StaffInformationForm, DepartmentForm, BookForm, StaffForm
from .models import StaffInformation, Department, Book, Staff


class StaffInformationCreateView(CreateView):
    model = StaffInformation
    form_class = StaffInformationForm
    template_name = 'myapp2/staff_information_create.html'
    # 飛ばせたいurls.pyのurlのname属性をいれる
    success_url = reverse_lazy('myapp2:staff_create')


class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'myapp2/department_create.html'
    success_url = reverse_lazy('myapp:home')


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'myapp2/book_create.html'
    success_url = reverse_lazy('myapp:home')


class StaffCreateView(CreateView):
    model = Staff
    form_class = StaffForm
    template_name = 'myapp2/staff_create.html'
    success_url = reverse_lazy('myapp2:staff_information_create')


class StaffListView(generic.ListView):
    model = Staff
    template_name = 'myapp2/staff_list.html'
# Create your views here.
