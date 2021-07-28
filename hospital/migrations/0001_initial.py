# Generated by Django 3.2.5 on 2021-07-27 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_number', models.CharField(max_length=50)),
                ('occupied', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=15)),
                ('kin', models.CharField(max_length=50, null=True)),
                ('kin_phone_no', models.CharField(max_length=15, null=True)),
                ('address', models.TextField()),
                ('SYMPTOMS', models.CharField(max_length=500, null=True)),
                ('prior_sickness', models.TextField()),
                ('dob', models.DateField(null=True)),
                ('doctors_notes', models.CharField(max_length=50, null=True)),
                ('doctors_visiting_time', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(max_length=50)),
                ('bed_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.bed')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
            ],
        ),
    ]