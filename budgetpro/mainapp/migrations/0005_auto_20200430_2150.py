# Generated by Django 3.0.3 on 2020-04-30 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20200424_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addexpense',
            name='user',
            field=models.CharField(max_length=120),
        ),
    ]
