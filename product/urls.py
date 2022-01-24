from django.urls import path
from product import views

app_name = 'product'

urlpatterns =[
    path('product/',views.product_page,name='product'),
    path('product/<pk>'),
   

]