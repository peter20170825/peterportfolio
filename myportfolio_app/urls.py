from django.urls import path
from myportfolio_app import views



urlpatterns = [
    path("", views.index, name='index'),
    path("resume/", views.resume, name='resume'),
    path("contact/", views.contact, name='contact'),
    path("ImagePage/<int:id>", views.ImagePage, name='ImagePage'),
    path("download/<int:id>", views.download, name='download'),
    path("thankyou", views.thankyou, name='thankyou'),

]
