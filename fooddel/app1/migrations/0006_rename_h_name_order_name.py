# Generated by Django 4.1.8 on 2023-05-04 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_order_delete_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='H_name',
            new_name='name',
        ),
    ]
