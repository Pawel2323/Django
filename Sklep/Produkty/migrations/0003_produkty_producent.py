# Generated by Django 4.1.1 on 2022-09-11 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0002_producent_alter_produkty_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkty',
            name='producent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Produkty.producent'),
        ),
    ]
