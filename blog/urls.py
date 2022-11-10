from django.http import HttpResponse;
from django.urls import path
from . import views
urlpatterns = [
      path('', views.shopMainPage),
       path('about/', views.about),
 path('contact/', views.contact),
  path('search/', views.search),
   path('tracker/', views.tracker),
    path('productview/', views.productview),
     path('checkout/', views.checkout)
]