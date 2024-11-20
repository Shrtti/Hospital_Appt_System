# Generated by Django 5.1.2 on 2024-10-10 19:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('dept_id', models.AutoField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospital_id', models.AutoField(primary_key=True, serialize=False)),
                ('hospital_name', models.CharField(max_length=100)),
                ('hospital_add', models.CharField(max_length=255)),
                ('hospital_phno', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('pat_id', models.AutoField(primary_key=True, serialize=False)),
                ('pat_name', models.CharField(max_length=100)),
                ('pat_phno', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('dr_id', models.AutoField(primary_key=True, serialize=False)),
                ('dr_name', models.CharField(max_length=100)),
                ('dr_phno', models.CharField(max_length=15)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.dept')),
            ],
        ),
        migrations.AddField(
            model_name='dept',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.hospital'),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_no', models.AutoField(primary_key=True, serialize=False)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appt_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('dr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.doctor')),
                ('pat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Presc',
            fields=[
                ('pres_no', models.AutoField(primary_key=True, serialize=False)),
                ('med_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=100)),
                ('staff_phno', models.CharField(max_length=15)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.dept')),
            ],
        ),
    ]