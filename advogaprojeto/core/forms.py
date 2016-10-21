from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from core.models import TemplateFile

class RegistrarUsuarioForm(forms.Form):
    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    senha = forms.CharField(required=True)
    telefone = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(RegistrarUsuarioForm, self).is_valid():
            self.adiciona_erro("Por Favor, verifique os dados informados")
            valid = False
        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)

class LogarForm(forms.Form):
    nome = forms.CharField(required=True)
    senha = forms.CharField(required=True)

class TemplateForm(ModelForm):
    class Meta:
        model = TemplateFile
        fields = ['nome','descricao','arquivo']