# Generated by Django 3.2.5 on 2021-07-15 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AlterField(
            model_name='variation',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
