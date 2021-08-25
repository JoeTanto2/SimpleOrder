# Generated by Django 3.2.5 on 2021-07-25 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(max_length=30)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='topping',
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='toppings',
            field=models.ManyToManyField(to='backend.Toppings'),
        ),
    ]