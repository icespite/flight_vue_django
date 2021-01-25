'''
@Author: IceSpite
@Date: 2020-03-16 19:43:10
@LastEditTime: 2020-03-24 23:15:05
'''
from django.urls import path
from user import views

urlpatterns = [
    path('getinform/', views.get_inform),
    path("search", views.search_flights),
    path('confirmInform/', views.confirm_inform),
    path('getalllocation/', views.get_all_location),
    path('searchbyflightnumber/',views.view_serch_flylog_byflightNumber),
    path('getallairline/', views.get_all_airline),
    path('buywait', views.buy_wait_post),
    path('buy', views.try_buy_post),
    path('getbuyinfo', views.get_all_buy_info),
    path('flightorder', views.flightorder),
    path('cancelbuy', views.cancel_buy),
    path('searchflightless',views.searchflightless),

]
