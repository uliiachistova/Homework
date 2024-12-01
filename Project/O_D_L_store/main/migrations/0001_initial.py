# Generated by Django 5.1.3 on 2024-12-01 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(max_length=50)),
                ('shape', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
    ]