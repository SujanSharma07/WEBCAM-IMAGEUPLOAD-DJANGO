# Generated by Django 3.2.5 on 2021-07-09 05:10

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TreeLeaf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('files', models.FileField(upload_to=main.models.getcurrentusername)),
                ('image', models.ImageField(upload_to=main.models.getcurrentusername)),
            ],
        ),
    ]
