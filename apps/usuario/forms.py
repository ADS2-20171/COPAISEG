from django.contrib.auth.forms import UserCreationForm

from ..account.models import User


class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
                'username',
                'email',
            ]
        labels = {
                'username': 'Nombre de usuario',
                'first_name': 'Nombre',
                'last_name': 'Apellidos',
                'email': 'Correo',
        }
