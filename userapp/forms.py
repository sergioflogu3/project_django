from django import forms

class FormFaculty(forms.Form):
    name = forms.CharField(
        label = 'Nombre',
        max_length = 40,
        required = False,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Ingresa el nombre de la Facultad'
            }
        )
    )

    description = forms.CharField(
        label = 'Descripción',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Ingresa la descripcion de la Facultad'
            }
        )

    )