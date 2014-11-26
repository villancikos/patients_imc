# coding=latin-1
from django import forms
from measurements.models import Patient


age_choices = [(x,str(x) + " Años") for x in range(25,46)]
weight_choices = [(y,str(y) + " Kilos") for y in range(40,121)]
sdg_choices = [(z, z) for z in range(1, 43)]

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields ='__all__'
        # ['patient_name', 'patient_last_name', 'patient_age_choices','patient_weight','patient_height','patient_sdg','patient_fum']





# class PatientForm(forms.Form):
#     patient_name = forms.CharField(label="Tu nombre:")
#     patient_last_name = forms.CharField(label="Tu apellido:")
#     patient_age_choices = forms.ChoiceField(label="Tu edad:",widget=forms.Select, choices= age_choices)
#     patient_weight = forms.ChoiceField(label="Tu peso:", widget=forms.Select, choices = weight_choices)
#     patient_height = forms.DecimalField(label="Tu altura en metros: (1.45 mts)")
#     patient_sdg = forms.ChoiceField(label = "Semanas de Gestacion", widget=forms.Select, choices = sdg_choices)
#     patient_fum = forms.DateField(label="Fecha de Ultima Menstruacion" , widget=SelectDateWidget)

# f = PatientForm(auto_id = False)
# print (f)
