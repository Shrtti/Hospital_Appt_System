# Generated by Django 5.1.2 on 2024-10-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0012_alter_doctor_dr_pwd_alter_hospital_hosp_pwd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='dr_phno',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='dr_pwd',
            field=models.CharField(default='pbkdf2_sha256$870000$kuI81GgOCDdkKgG0yFnvLm$pNIXcgD45spk8NrgCQ6zkjKDNVp9XAv1ouECfC1Wv2s=', max_length=128),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hosp_pwd',
            field=models.CharField(default='pbkdf2_sha256$870000$pxgoumK3t4FMzzhS97Sj0Q$xYQGRCi5IFHKbUktGUXlpmp4c8GgLgywOrmgYDuFBRw=', max_length=128),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_phno',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pat_phno',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pat_pwd',
            field=models.CharField(default='pbkdf2_sha256$870000$wyctgYWE2pDTUW9vHfxLEd$n2+Hwm4bwP3FwQyLCm76aMhDNPKVazdFT5iTaowHhPg=', max_length=128),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_phno',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_pwd',
            field=models.CharField(default='pbkdf2_sha256$870000$sl9KN002ErCY2QLvlrdstd$+Q8WJnx6G50N8U53W469bMl1pkUR7nd2rB4eHayGNg0=', max_length=128),
        ),
    ]
