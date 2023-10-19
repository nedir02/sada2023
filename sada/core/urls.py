from django.urls import path
from .views import *

urlpatterns = [
    # path('', ViewProduct.as_view())
    path('', index, name="index"),
    path('about-us/', about_us),
    path('history/', history, name='history'),
    path('contact_us/', contact_us, name='contact_us'),
    path('product/', product, name = 'product')


]


