# Generated by Django 5.1.2 on 2024-10-13 06:33

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_sign_up'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('address', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=12)),
                ('date', models.DateField(default=datetime.datetime(2024, 10, 13, 12, 3, 45, 554974))),
                ('status', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.sign_up')),
            ],
        ),
    ]
