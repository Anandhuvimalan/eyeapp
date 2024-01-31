# Generated by Django 4.2.7 on 2023-12-02 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eyeapp', '0010_alter_doctordetails_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_content', models.TextField()),
                ('service', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='eyeapp.service')),
            ],
        ),
    ]
