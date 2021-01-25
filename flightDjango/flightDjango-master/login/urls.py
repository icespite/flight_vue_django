from django.urls import path
from login import views

urlpatterns = [
    path('login', views.login),
    path('info/', views.get_info),
    path('table/list', views.get_table_list),
    path('logout', views.logout),
]
