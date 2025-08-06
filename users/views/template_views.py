from django.views.generic import TemplateView, FormView
from django.http import HttpResponseBadRequest
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy

from users.forms import RegisterForm


class RegisterUserView(FormView):
    template_name = "auth/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RegisterForm()

        return context
    
    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, "Registration successful!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # Add this for debugging
        print("Form errors:", form.errors)
        return super().form_invalid(form)