# Generated by Django 4.1.8 on 2023-05-08 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_rename_orderd_ord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ord',
            name='type',
            field=models.CharField(max_length=500),
        ),
    ]
