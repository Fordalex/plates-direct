# Generated by Django 3.1.5 on 2021-02-07 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_regplate_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='reg_plate',
        ),
        migrations.AddField(
            model_name='order',
            name='reg_plate',
            field=models.CharField(default='', editable=False, max_length=256),
        ),
        migrations.DeleteModel(
            name='RegPlate',
        ),
    ]
