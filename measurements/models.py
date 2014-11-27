from django.db import models
# coding=latin-1


class Patient(models.Model):

    age_choices = [(x,x) for x in range(25,46)]
    weight_choices = [(y,y) for y in range(40,121)]
    sdg_choices = [(z, z) for z in range(1, 43)]

    patient_name = models.CharField(
                "Tu Nombre:",
                max_length = 40,
                help_text="Por favor inserta tu nombre."
    )

    patient_last_name = models.CharField(
                "Tu Apellido:",
                max_length = 60,
                help_text="Por favor inserta tu apellido."
    )

    patient_age_choices = models.PositiveSmallIntegerField(
                "Tu Edad:",
                max_length = 2,
                choices= age_choices,
                help_text="Ingresa tu edad de la lista desplegable."
    )

    patient_weight = models.PositiveSmallIntegerField(
                "Tu Peso:",
                max_length=3,
                choices = weight_choices,
                help_text="Selecciona tu peso de la lista. Cerrado y en Kilogramos (55)"
    )

    patient_height = models.DecimalField(
                "Tu altura en metros (ej: 1.45mts)",
                max_digits = 3,
                decimal_places = 2,
                help_text="Selecciona tu altura en metros y con dos decimales. (1.68)"
    )
    # patient_height = models.FloatField(
    #             validators=[MinValueValidator(1.45), MaxValueValidator(1.90)]

    # Code grabbed from:
    # http://blog.p3infotech.in/2013/enforcing-minimum-and-maximum-values-in-django-model-fields/


    patient_sdg = models.PositiveSmallIntegerField(
                "Semanas de Gestación",
                choices= sdg_choices,
                help_text="SDG = Semanas de Gestacion."
    )
    # SDG = Semanas de Gestacion

    patient_fum = models.DateField(
                "Fecha de Última Menstruación",
                help_text="FUM = Fecha de Ultima Menstruacion"
    )

    modified_date = models.DateField(auto_now=True)

    @property
    def patient_imc(self):
        return self.patient_weight / (self.patient_height**2)
    # Indice de Masa Corporal; ( Peso(Kg) / Altura^2(mts) ) en metros ^ 2

    ####### Probando si es mejor opcion #######
    @property
    def patient_status(self):
        if self.patient_imc <= 18.5:
            return 'Bajo'
        elif self.patient_imc < 24.9 and self.patient_imc >= 18.5:
            return 'Normal'
        elif self.patient_imc < 29.9 and self.patient_imc >= 25.0:
            return 'Sobrepeso'
        elif self.patient_imc < 30.0 and self.patient_imc >= 34.9:
            return 'Obesidad'
        elif self.patient_imc < 35.0 and self.patient_imc >= 39.9:
            return 'Obesidad Grado 2'
        else:
            return 'Obesidad Grado 3'

    def __unicode__(self):
        return "ID:"+str(self.id) + " ,Nombre:" + self.patient_name + " ,Apellido:" + self.patient_last_name + ", IMC: " + str("{0:.2f}".format(self.patient_imc))



