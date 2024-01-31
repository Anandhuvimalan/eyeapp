from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('diagnostic-testing', views.subpage1, name='diagnostic-testing'),
    path('eye-condition-treatments', views.subpage2,
         name='eye-condition-treatments'),
    path('categories', views.categories, name='categories'),
    path('categories/<slug:slug>/', views.category_detail, name='category_detail'),
    path('services', views.services, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('about', views.about, name='about'),
    path('doctor', views.doctors, name='doctors'),
    path('doctor/<slug:slug>/', views.doctor_detail, name='doctor_detail'),
    path('gallery', views.gallery_view, name='gallery'),
    path('blogs/', views.blog_view, name='blog'),
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('reviews/', views.review_list, name='reviews'),
    path('contact/', views.contact, name='contact'),


]
