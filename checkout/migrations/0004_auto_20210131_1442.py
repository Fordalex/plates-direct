# Generated by Django 3.1.5 on 2021-01-31 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20210131_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegPlate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_plate', models.CharField(max_length=32)),
                ('log_book', models.FileField(blank=True, null=True, upload_to='log_book')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='reg_plate',
        ),
        migrations.AddField(
            model_name='order',
            name='reg_plate',
            field=models.ManyToManyField(to='checkout.RegPlate'),
        ),
    ]
