from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('about/', views.about, name='about'),
    # path('djangoform/', views.djangoform, name='djangoform'),
    # path('djangoform/', views.validdata, name='djangoform'),
    path('djangoform/', views.validPassword, name='djangoform'),
]