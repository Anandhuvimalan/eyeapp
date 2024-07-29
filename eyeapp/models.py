from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return self.name


class CategoryDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.OneToOneField(
        Category, related_name='details', on_delete=models.CASCADE)
    category_content = models.TextField()

    def __str__(self):
        return f"{self.category.name}'s Details"


class Icon(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(
        Category, related_name='icons', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.FileField(upload_to='category_icons/')

    def __str__(self):
        return self.name


class Service(models.Model):
    id = models.IntegerField(primary_key=True)
    icon = models.ForeignKey(
        Icon, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='service_images/')
    featured = models.BooleanField(default=False)
    service_nav = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class Doctor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='doctor_images/')

    def __str__(self):
        return self.name


class DoctorDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    doctor = models.OneToOneField(
        Doctor, related_name='details', on_delete=models.CASCADE)
    main_description = models.TextField(blank=True)
    about_description = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    expertise = models.TextField(blank=True)
    practice = models.TextField(blank=True)

    def __str__(self):
        return f"{self.doctor.name}'s Details"


class ServiceDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    service = models.OneToOneField(
        Service, related_name='details', on_delete=models.CASCADE)
    service_content = models.TextField()

    def __str__(self):
        return f"{self.service.name}'s Details"


class Gallery(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return self.name


class Mizhi(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='mizhi_images/')

    def __str__(self):
        return self.name


class Equipment(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='equipment_images/')

    def __str__(self):
        return self.name

#  blogs


class BlogCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    content = models.TextField()

    # Add any other fields or methods as needed

    def __str__(self):
        return self.title


class Review(models.Model):
    id = models.IntegerField(primary_key=True)
    patient_name = models.CharField(max_length=255)
    content = models.TextField()
    what_doctor = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Review_images/')

    def __str__(self):
        return self.patient_name


class ManagementTeam(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='management_team_images/')

    def __str__(self):
        return self.name


class ManagementTeamDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    team_member = models.OneToOneField(
        ManagementTeam, related_name='details', on_delete=models.CASCADE)
    main_description = models.TextField(blank=True)
    about_description = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    expertise = models.TextField(blank=True)
    responsibilities = models.TextField(blank=True)

    def __str__(self):
        return f"{self.team_member.name}'s Details"
