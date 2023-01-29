from django.urls import path

from myforms import views


app_name = 'myforms'

urlpatterns = [
    path('thanks/', views.thanks, name='thanks'),
    path('name/', views.get_name, name='name'),
    path('contact/', views.get_contact_data, name='contact'),
]
