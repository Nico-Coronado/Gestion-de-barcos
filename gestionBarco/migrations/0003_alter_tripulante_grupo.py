# Generated by Django 3.2.6 on 2021-09-06 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionBarco', '0002_auto_20210831_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripulante',
            name='grupo',
            field=models.CharField(choices=[('Grupo 1', 'Grupo 1'), ('Grupo 2', 'Grupo 2')], max_length=50),
        ),
    ]
