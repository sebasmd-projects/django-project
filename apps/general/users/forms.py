from django import forms
from django.contrib.auth import authenticate
from django.utils. translation import gettext as _
from . import models
from .functions import password_validation


class UserRegisterForm(forms.ModelForm):

    username = forms.CharField(
        label=_('Usuario'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'placeholder': _('Usuario'),
                'class': 'form-control',
                'id': 'register_id_username'
            }
        )
    )

    email = forms.CharField(
        label=_('Correo'),
        required=True,
        widget=forms.EmailInput(
            attrs={
                'type': 'email',
                'placeholder': _('Correo'),
                'class': 'form-control',
                'id': 'register_id_email'
            }
        )
    )

    phone = forms.CharField(
        label=_('Celular'),
        required=True,
        widget=forms.NumberInput(
            attrs={
                'type': 'tel',
                'placeholder': _('Celular'),
                'class': 'form-control',
                'id': 'register_id_phone'
            }
        )
    )

    names = forms.CharField(
        label=_('Nombres'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'placeholder': _('Nombres'),
                'class': 'form-control',
                'id': 'register_id_names'
            }
        )
    )

    surname = forms.CharField(
        label=_('Apellidos'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'placeholder': _('Apellidos'),
                'class': 'form-control',
                'id': 'register_id_surname'
            }
        )
    )

    birthday = forms.DateField(
        label=_('Cumpleaños'),
        required=True,
        widget=forms.NumberInput(
            attrs={
                'type': 'date',
                'placeholder': _('Cumpleaños'),
                'class': 'form-control',
                'id': 'register_id_birthday'
            }
        )
    )

    newsletter = forms.BooleanField(
        label=_('Recibir Información'),
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'type': 'checkbox',
                'value': 'suscribe',
                'id': 'register_id_newsletter'
            }
        )
    )

    privacy = forms.BooleanField(
        label=_('Términos y Condiciones'),
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                'type': 'checkbox',
                'id': 'register_id_privacy'
            }
        )
    )

    password = forms.CharField(
        label=_('Contraseña'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'placeholder': _('Contraseña'),
                'class': 'form-control',
                'id': 'register_id_password'
            }
        )
    )

    repeat_password = forms.CharField(
        label=_('Repetir contraseña'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'placeholder': _('Repetir contraseña'),
                'class': 'form-control',
                'id': 'register_id_repeat_password'
            }
        )
    )

    class Meta:
        model = models.User
        fields = (
            'username',
            'email',
            'phone',
            'names',
            'surname',
            'birthday',
            'gender',
            'newsletter',
            'privacy',
        )

    def clean_repeat_password(self):
        password_validation(
            self, self.cleaned_data['password'], self.cleaned_data['repeat_password'])


class UserLoginForm (forms.Form):
    username = forms.CharField(
        label=_('Usuario'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'placeholder': _('Usuario'),
                'class': 'form-control',
                'id': 'login_id_username'
            }
        )
    )

    password = forms.CharField(
        label=_('Contraseña'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'placeholder': _('Contraseña'),
                'class': 'form-control',
                'id': 'login_id_password'
            }
        )
    )

    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError(
                _('Los datos de acceso no son correctos'))

        return self.cleaned_data


class UpdatePasswordForm (forms.Form):
    password = forms.CharField(
        label=_('Contraseña Actual'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'placeholder': _('Contraseña Actual'),
                'class': 'form-control',
                'id': 'actual_id_password'
            }
        )
    )

    new_password = forms.CharField(
        label=_('Contraseña Nueva'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'placeholder': _('Contraseña Nueva'),
                'class': 'form-control',
                'id': 'new_id_password'
            }
        )
    )

    confirm_password = forms.CharField(
        label=_('Confirmar Contraseña'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'placeholder': _('Confirmar Contraseña'),
                'class': 'form-control',
                'id': 'confirm_id_password'
            }
        )
    )

    def clean_repeat_password(self):
        password_validation(
            self, self.cleaned_data['new_password'], self.cleaned_data['confirm_password'])



class VerificationCodeForm(forms.Form):
    verification_code = forms.CharField(
        label=_('Código de verificación'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'placeholder': _('Código de verificación'),
                'class': 'form-control',
                'id': 'verfication_code_id'
            }
        )
    )

    
    def __init__(self, pk, *args, **kwargs):
        self.user_id = pk
        super(VerificationCodeForm, self).__init__(*args, **kwargs)
    

    def clean_verificationcode(self):
        cod = self.cleaned_data['verification_code']

        if len(cod) == 4:
            active = models.User.objects.cod_validation(
                self.user_id['pk'],
                cod
            )
            if not active:
                raise forms.ValidationError(_('El código ingresado no es correcto'))
        else:
            raise forms.ValidationError(_('El código ingresado no es correcto'))
