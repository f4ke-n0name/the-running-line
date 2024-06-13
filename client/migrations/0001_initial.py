# Generated by Django 5.0.6 on 2024-06-11 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=42)),
                ('text', models.TextField()),
                ('content', models.FileField(upload_to='videos/')),
            ],
        ),
    ]