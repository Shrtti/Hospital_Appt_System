# Generated by Django 5.1.2 on 2024-10-12 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0004_alter_doctor_dr_pwd_alter_hospital_hosp_pwd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='dr_pwd',
            field=models.CharField(default='pbkdf2_sha256$870000$4PM9vpcgYk8a8LeSx74sdi$R7/sRef17+WoVv6lg45aoCrQUrf23OiRyOiWsojsr3E=', max_length=128),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hosp_pwd',
            field=models.CharField(default='pbkdf2_sha256$870000$5zF1jwilNPr7o3HBZHPauP$b54jdAaKW5Tz7Df0v5LrxXI1degejvev8ePTRE65JZ4=', max_length=128),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pat_pwd',
            field=models.CharField(default='pbkdf2_sha256$870000$IhFX70jlPeindkHTmbkJAv$su/Fvlg2BirvR4XhSv2Kg/im+azsNffzYHFbXIUGxuw=', max_length=128),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_pwd',
            field=models.CharField(default='pbkdf2_sha256$870000$aKjNMjgRO6aJlup6xzVutd$tYiAJuA13ChGVlS4Rpzj1TkbKmOgbuMMSOrHpl0/+yI=', max_length=128),
        ),
    ]
