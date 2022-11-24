from contextlib import ContextDecorator
from faulthandler import cancel_dump_traceback_later
from mailbox import NoSuchMailboxError
from tkinter import Widget
from django import forms
class FormularioMedico(forms.Form):
    ESPECIALIDADES=(
        (1, 'Cardiologia'),
        (2, 'Medicina Interna'),
        (3, 'Medico General'),
        (4, 'Ortopedia'),
        (5, 'Pediatria')
    )
    JORNADAS=(
        (1, '06:00am a 02:00pm'),
        (2, '02:00pm a 10:00pm'),
        (3, '10:00pm a 06:00am')
    )
    SEDES=(
        (1, 'LOS MOLINOS'),
        (2, 'ALMACENTRO'),
        (3, 'PUNTO CLAVE')
    )
    nombre=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=15
    )
    apellidos=forms.CharField(
    widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=35
    )
    cedula=forms.CharField(
    widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=10
    )
    tarjetaProfesional=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=20
    )
    especialidad=forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices=ESPECIALIDADES
    )
    jornada=forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices=JORNADAS
    )
    contacto=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=20
    )
    sede=forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices=SEDES
    )
