# Generated by Django 4.0.5 on 2023-01-14 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=200)),
                ('categoria', models.CharField(max_length=200)),
                ('precio', models.PositiveIntegerField(max_length=10000)),
            ],
        ),
    ]