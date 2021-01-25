from django.urls import path
from manager import views

urlpatterns = [
    path('modefylocation', views.modietfy_location),
    path('addlocation', views.add_location),
    path('deletelocation', views.delete_location),
    path('modefyairline', views.modify_airline),
    path('addairline', views.add_airline),
    path('deleteairline', views.delete_airline),
    path('modifyflight',views.modifyFlight),
    path('cancelflight', views.cancelflight),
    path('addflight',views.addFlight),
    path('deleteflight',views.deleteFlight),

]
