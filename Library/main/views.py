from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views import generic
from .forms import UserForm,LibAdminForm

# Create your views here.

app_name = 'main'


def main(request):
    return render(request, 'main/index.html')


class UserFormView(generic.FormView):
    form_class = UserForm
    template_name = 'main/create_user.html'

    def form_valid(self, form):
        form.save()

        return super(UserFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse('success')


def success(request):
    return render(request, "main/success.html")


def lib_user(request):
    form = LibAdminForm()
    if request.method == 'POST':
        form = LibAdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'main/lib_user.html', context)