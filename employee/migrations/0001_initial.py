# Generated by Django 4.0.4 on 2022-04-29 16:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComputationResourceType',
            fields=[
                ('ramsizegb', models.IntegerField(choices=[('4', '4'), ('8', '8'), ('16', '16')], verbose_name='Ram')),
                ('storagesizegb', models.IntegerField(choices=[('20', '20'), ('40', '40'), ('72', '72')], verbose_name='Storage')),
                ('vcpucorescount', models.IntegerField(choices=[('2', '2'), ('4', '4'), ('6', '6')], verbose_name='CPU cores')),
                ('firmwarversion', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^[0-9]{3}.[a-zA-Z]{3}$')], verbose_name='Firmware Version')),
                ('hardwarversion', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]{1}[0-9]{1}[a-zA-Z]{3}[0-9]{2}$')], verbose_name='Hardware Version')),
                ('partnumber', models.IntegerField(primary_key=True, serialize=False, verbose_name='Part Number')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('name', models.CharField(max_length=82, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=100)),
                ('email_ID', models.EmailField(max_length=50, unique=True)),
                ('phone_number', models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]{10}$')])),
            ],
        ),
        migrations.CreateModel(
            name='ComputationResource',
            fields=[
                ('name', models.CharField(max_length=82, primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.customer')),
                ('part_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.computationresourcetype')),
            ],
        ),
    ]
