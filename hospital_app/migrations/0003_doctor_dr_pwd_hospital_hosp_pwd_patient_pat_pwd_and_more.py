# Generated by Django 5.1.2 on 2024-10-12 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0002_alter_patient_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='dr_pwd',
            field=models.CharField(default='pbkdf2_sha256$870000$XeqcX43PTgugr9NQBRZ7G5$my8P0qWG4fvqW5eO4dccBhCL9eImdmKpVYc5YpVnrKI=', max_length=128),
        ),
        migrations.AddField(
            model_name='hospital',
            name='hosp_pwd',
            field=models.CharField(default='pbkdf2_sha256$870000$rRxsY7tZhRgxrUBVrjtu1P$MUGT7RAHS41lkC+iFxvvWwTS30KM/RmQmG0rGUoNmFk=', max_length=128),
        ),
        migrations.AddField(
            model_name='patient',
            name='pat_pwd',
            field=models.CharField(default='pbkdf2_sha256$870000$3HHC7CMhY2lOtDXodNpthj$1kvoCHKgB6TyEOxUNQifmXrA936QRvPwWpXZEa1fAu0=', max_length=128),
        ),
        migrations.AddField(
            model_name='staff',
            name='staff_pwd',
            field=models.CharField(default='pbkdf2_sha256$870000$yoxnnzQtvjFJSbgLD5JF8N$HqnT+v8CRixJtykvSLht5fiRQC/n2dcxR/I+8U87Xuc=', max_length=128),
        ),
        migrations.AlterModelTable(
            name='appointment',
            table='hospital_app_appointment',
        ),
        migrations.AlterModelTable(
            name='doctor',
            table='hospital_app_doctor',
        ),
        migrations.AlterModelTable(
            name='hospital',
            table='hospital_app_hospital',
        ),
        migrations.AlterModelTable(
            name='staff',
            table='hospital_app_staff',
        ),
    ]