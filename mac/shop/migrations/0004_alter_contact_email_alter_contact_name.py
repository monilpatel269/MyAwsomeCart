# Generated by Django 4.0.3 on 2022-04-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
