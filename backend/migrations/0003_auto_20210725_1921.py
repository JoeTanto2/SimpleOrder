# Generated by Django 3.2.5 on 2021-07-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210725_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('in_stock', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('is being prepared', 'is being prepared'), ('ready', 'ready'), ('is being delivered', 'is being delivered'), ('delivered', 'delivered')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='toppings',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
    ]