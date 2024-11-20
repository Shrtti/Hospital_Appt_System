# Generated by Django 5.1.2 on 2024-10-14 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0015_alter_doctor_dr_pwd_alter_hospital_hosp_pwd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='dr_pwd',
            field=models.CharField(default='pbkdf2_sha256$870000$DXCT9hy73FlQBbVB0e1UaT$xPgQnNSUSHBXrFPuz9EN2L33LadIw+wGYs1kMmyyNM4=', max_length=128),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hosp_pwd',
            field=models.CharField(default='pbkdf2_sha256$870000$fu6XPxhSTaTUU8pcKezQqg$LCe3Xj8GeImSkHZrXP8evUAJeV/Rz/zu2WEGsCGoiQc=', max_length=128),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pat_pwd',
            field=models.CharField(default='pbkdf2_sha256$870000$vczOskLuGclENRTMMNl1a6$qSr4fKlG4EU3Rtnx1AMYtKuxr4HtiHaSUelKzdrVajU=', max_length=128),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_pwd',
            field=models.CharField(default='pbkdf2_sha256$870000$vLn9gwGATZq8MmjQzE0Zf8$BKTmyvtQcEYk/kScOpJxwQE5Ixj+wroUqZDUPlS9TtY=', max_length=128),
        ),
    ]