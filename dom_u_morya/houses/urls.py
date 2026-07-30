from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.houses_list, name='houses_list'),
    path('<int:house_id>/', views.house_detail, name='house_detail')
]
