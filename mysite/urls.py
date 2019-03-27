from django.urls import path
from . import views

app_name = 'mysite'
urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('skills/', views.skills, name="skills"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('services/', views.services, name="services"),


]
