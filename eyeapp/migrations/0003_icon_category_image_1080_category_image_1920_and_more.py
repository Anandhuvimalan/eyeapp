# Generated by Django 4.2.7 on 2023-11-24 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eyeapp', '0002_alter_categoryicon_icon_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.FileField(upload_to='category_icons/')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='image_1080',
            field=models.ImageField(blank=True, upload_to='category_images_1080/'),
        ),
        migrations.AddField(
            model_name='category',
            name='image_1920',
            field=models.ImageField(blank=True, upload_to='category_images_1920/'),
        ),
        migrations.AddField(
            model_name='category',
            name='image_500',
            field=models.ImageField(blank=True, upload_to='category_images_500/'),
        ),
        migrations.AddField(
            model_name='category',
            name='image_800',
            field=models.ImageField(blank=True, upload_to='category_images_800/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='category_images/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='CategoryIcon',
        ),
        migrations.AddField(
            model_name='icon',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='icons', to='eyeapp.category'),
        ),
    ]
