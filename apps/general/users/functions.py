import random
import string
from django.utils. translation import gettext as _


def password_validation(self, p1, p2):
    password1 = p1
    password2 = p2

    min = 6
    lowerc = False
    upperc = False
    num = False
    special = False
    special_characters = "!@#$%^&*()-+?_=,<>/\{\}\[\]\\|:;\"'.~´¡%^1234567890"

    if any(c in special_characters for c in password1):
        special = True

    for c in password1:
        if c.islower():
            lowerc = True
        elif c.isupper():
            upperc = True
        elif c.isdigit():
            num = True

    if len(password1) < min:
        self.add_error('repeat_password', _(
            'La contraseña debe tener al menos 6 caracteres'))

    elif password1 != password2:
        self.add_error('repeat_password', _('Las contraseñas no coinciden'))

    elif lowerc == False and upperc == False:
        self.add_error('repeat_password', _(
            'La contraseña debe contener al menos una letra'))

    elif special == False and num == False:
        self.add_error('repeat_password', _(
            'La contraseña debe contener al menos un caracter especial'))


def generate_random_code(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
