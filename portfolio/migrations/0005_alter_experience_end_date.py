# Generated by Django 3.2.3 on 2021-05-29 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_education_degree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]
