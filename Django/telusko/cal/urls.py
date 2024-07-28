from django.urls import path
from . import views
# from django.urls import
urlpatterns = [
    path('', include('calc.urls')),
    path('', views.home, name="home")
]
