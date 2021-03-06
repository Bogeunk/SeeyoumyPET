from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

signup = CreateView.as_view(
    form_class=UserCreationForm,
    template_name='account/form.html',
    success_url=settings.LOGIN_URL,
)

login = LoginView.as_view(
    template_name='account/form.html',
)

logout = LogoutView.as_view(
    next_page=settings.LOGIN_URL
)

@login_required
def profile(request):
    return render(request, 'account/profile.html')
    pass