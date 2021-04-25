from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sight_id>/', views.detail, name='detail'),
    path('thanks/', views.thanks, name='thanks')
]
