# from django.urls import path
# from .import views

# urlpatterns =[
#     path('',views.home)

# ]
from django.urls import path
from . import views  # Ensure this import is correct

urlpatterns = [
    # path('', views.home, name='home'),
    path('',views.contact)
]
