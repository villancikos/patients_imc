# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0004_patient_patient_fum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_age_choices',
            field=models.PositiveSmallIntegerField(help_text=b'Ingresa tu edad de la lista desplegable.', max_length=2, verbose_name=b'Tu edad:', choices=[(25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_fum',
            field=models.DateField(help_text=b'FUM = Fecha de Ultima Menstruacion', verbose_name=b'Fecha de \xc3\x9altima Menstruaci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_height',
            field=models.DecimalField(help_text=b'Selecciona tu altura en metros y con dos decimales. (1.68)', verbose_name=b'Tu altura en metros (ej: 1.45mts)', max_digits=3, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_last_name',
            field=models.CharField(help_text=b'Por favor inserta tu apellido.', max_length=60, verbose_name=b'Tu Apellido:'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_name',
            field=models.CharField(help_text=b'Por favor inserta tu nombre.', max_length=40, verbose_name=b'Tu Nombre:'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_sdg',
            field=models.PositiveSmallIntegerField(help_text=b'SDG = Semanas de Gestacion.', verbose_name=b'Semanas de Gestaci\xc3\xb3n', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_weight',
            field=models.PositiveSmallIntegerField(help_text=b'Selecciona tu peso de la lista. Cerrado y en Kilogramos (55)', max_length=3, choices=[(40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59), (60, 60), (61, 61), (62, 62), (63, 63), (64, 64), (65, 65), (66, 66), (67, 67), (68, 68), (69, 69), (70, 70), (71, 71), (72, 72), (73, 73), (74, 74), (75, 75), (76, 76), (77, 77), (78, 78), (79, 79), (80, 80), (81, 81), (82, 82), (83, 83), (84, 84), (85, 85), (86, 86), (87, 87), (88, 88), (89, 89), (90, 90), (91, 91), (92, 92), (93, 93), (94, 94), (95, 95), (96, 96), (97, 97), (98, 98), (99, 99), (100, 100), (101, 101), (102, 102), (103, 103), (104, 104), (105, 105), (106, 106), (107, 107), (108, 108), (109, 109), (110, 110), (111, 111), (112, 112), (113, 113), (114, 114), (115, 115), (116, 116), (117, 117), (118, 118), (119, 119), (120, 120)]),
        ),
    ]
