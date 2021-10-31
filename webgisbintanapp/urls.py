from django.urls import path
from webgisbintanapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bataskabupaten/', views.BataskabupatenData, name='kabupaten'),
]


