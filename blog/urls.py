from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
]