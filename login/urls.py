from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout,name='logout'),
    path('admindash/',views.admindash,name='admindash'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('add/',views.add, name='add'),
    path('edit/',views.edit, name='edit'),
    path('update/<str:id>',views.update,name='update'),
    path('delete/<str:id>',views.delete,name='delete')
]
