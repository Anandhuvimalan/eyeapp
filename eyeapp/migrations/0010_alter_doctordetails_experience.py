# Generated by Django 4.2.7 on 2023-11-30 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eyeapp', '0009_alter_doctordetails_expertise_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctordetails',
            name='experience',
            field=models.TextField(),
        ),
    ]