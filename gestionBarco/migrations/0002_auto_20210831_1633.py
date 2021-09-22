# Generated by Django 3.2.6 on 2021-08-31 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionBarco', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barco',
            name='tripulante',
        ),
        migrations.AddField(
            model_name='tripulante',
            name='barco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionBarco.barco'),
        ),
    ]