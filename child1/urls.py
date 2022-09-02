from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('cricket/', views.cricket, name='cricket'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('cricket/add/', views.cricketadd, name='cricketadd'),
    path('cricket/add/addrecord/', views.cricketaddrecord, name='addrecord'),
    path('cricket/delete/<int:id>', views.cricketdelete, name='delete'),
    path('cricket/update/<int:id>', views.cricketupdate, name='cricketupdate'),
    path('cricket/update/updaterecord/<int:id>', views.cricketupdaterecord, name='cricketupdaterecord')
]

