from django.urls import path

from users.views.template_views import RegisterUserView


urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register-template"),
]