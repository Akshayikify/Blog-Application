from django.urls import path
from . import views
urlpatterns=[
    path('create/',views.create_product,name='create'),
    path('',views.product_list,name='product_list'),
    path('<int:pk>/edit/',views.edit_product,name='edit'),
    path('<int:pk>/delete/',views.delete_product,name='delete'),
    path('<int:pk>/',views.product_details,name='product_details')
]