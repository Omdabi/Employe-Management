from django.urls import path
from .import views

urlpatterns = [
    path('',views.base, name='base'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.logout, name='logout'),
    path('adddepartment/',views.adddepartment,name='adddepartment'),
    path('addrole/',views.addrole,name='addrole'),
    path('addemploye/',views.addemploye,name='addemploye'),
    path('ddetails/',views.ddetails,name='ddetails'),
    path('rdetails/',views.rdetails,name='rdetails'),
     path('edetails/',views.edetails,name='edetails'),
     path('ddelete/<int:did>/',views.ddelete,name='ddelete'),
     path('dedit/<int:did>/',views.dedit,name='dedit')
    

]
