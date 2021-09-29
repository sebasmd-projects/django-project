from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from django.views.generic import View
from django.views.generic.edit import (
    FormView,
)

from .forms import (
    UserRegisterForm,
    UserLoginForm,
    UpdatePasswordForm,
    VerificationCodeForm
)

from .functions import generate_random_code

from .models import User


class UserRegisterView(FormView):
    template_name = "general/user/register.html"
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        v_code = generate_random_code()

        user = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password'],
            phone=form.cleaned_data['phone'],
            names=form.cleaned_data['names'],
            surname=form.cleaned_data['surname'],
            birthday=form.cleaned_data['birthday'],
            gender=form.cleaned_data['gender'],
            newsletter=form.cleaned_data['newsletter'],
            privacy=form.cleaned_data['privacy'],
            verification_code=v_code
        )

        
        subject = 'Código de verificación'
        message = 'Hola {}.\nTu código de verificación es: {}'.format(
            form.cleaned_data['names'], 
            v_code,
        )
        email_sender = 'info@sebasmd.com'

        send_mail(
            subject,
            message,
            email_sender,
            [form.cleaned_data['email'], ]
        )

        return HttpResponseRedirect(
            reverse(
                'users_app:user-verification',
                kwargs={'pk': user.id}
            )
        )


class UserLoginView(FormView):
    template_name = "general/user/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy('about_app:about')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(UserLoginView, self).form_valid(form)


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )


class UpdatePassword(LoginRequiredMixin, FormView):
    template_name = "general/user/change-password.html"
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:user-login')
    login_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        usr = self.request.user
        user = authenticate(
            username=usr.username,
            password=form.cleaned_data['password']
        )

        if user:
            new_password = form.cleaned_data['new_password']
            usr.set_password(new_password)

        logout(self.request)
        return super(UpdatePassword, self).form_valid(form)


class VerificationCodeView(FormView):
    template_name = 'general/user/validation-code.html'
    form_class = VerificationCodeForm
    success_url = reverse_lazy('users_app:user-login')

    def get_form_kwargs(self):
        kwargs = super(VerificationCodeView, self).get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs['pk'],
        })
        return kwargs

    def form_valid(self, form):

        User.objects.filter(
            id=self.kwargs['pk']
        ).update(
            is_active=True
        )
        
        return super(VerificationCodeView, self).form_valid(form)
