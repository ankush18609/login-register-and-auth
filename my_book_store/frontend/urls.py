from django.urls import include,path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
      path
      ('', views.home, name='home'),
    
    path
    ('signup/', views.signup, name='signup'),
        path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        views.activate, name='activate'),  
        path('login/',views.Login,name='login'),
        path('logout',views.Logout,name='logout'),
    
]