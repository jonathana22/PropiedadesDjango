# Generated by Django 3.1 on 2020-12-01 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='imgane',
            field=models.ImageField(null=True, upload_to='propiedades'),
        ),
    ]
