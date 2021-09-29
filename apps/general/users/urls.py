from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from . import views

app_name = "users_app"


urlpatterns = [
    path(
        _('registro/'), 
        views.UserRegisterView.as_view(), 
        name='user-register',
    ),
    path(
        _('iniciar-sesion/'), 
        views.UserLoginView.as_view(), 
        name='user-login',
    ),
    path(
        _('cerrar-sesion/'), 
        views.UserLogoutView.as_view(), 
        name='user-logout',
    ),
    path(
        _('cambiar-contraseña/'), 
        views.UpdatePassword.as_view(), 
        name='user-update-password',
    ),
    path(
        _('verificar-usuario/<pk>/'), 
        views.VerificationCodeView.as_view(), 
        name='user-verification',
    ),
]
