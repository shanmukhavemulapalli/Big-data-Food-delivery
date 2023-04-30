# Generated by Django 4.1.8 on 2023-04-29 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_userinfo_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iname', models.CharField(max_length=50)),
                ('price', models.IntegerField(max_length=30)),
                ('image', models.ImageField(upload_to='product')),
            ],
        ),
    ]