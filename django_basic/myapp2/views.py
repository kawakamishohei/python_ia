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


class StaffDetailView(generic.DetailView):
    model = Staff
    template_name = 'myapp2/staff_detail.html'

    def get_object(self, queryset=None):
        # self.kwargsは、URL内の int:pkといった部分が入っている
        staff = Staff.objects.get(pk=self.kwargs['pk'])
        # →Staff.objects.get(pk=1)  # 今回、URLは/staff_detail/1/
        # →Staff.objects.get(id=1)  # pkというのは、primarykeyのこと。今回ならidフィールドのこと
        return staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        staff = self.get_object()
        context['books'] = staff.rented_books.all()
        return context

class StaffListView(generic.ListView):
    model = Staff
    template_name = 'myapp2/staff_list.html'
# Create your views here.
