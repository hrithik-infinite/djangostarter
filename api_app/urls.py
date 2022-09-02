from django.urls import path
from . import views


urlpatterns =[
   path("cart-items/", views.CartItemViews.as_view()),
   path("cart-items/<int:id>", views.CartItemViews.as_view()),
   path("cricket/", views.CricketTeamListView.as_view()),
   path("cricket/<int:id>", views.CricketTeamListView.as_view()),
   path('cricket/add/', views.addPlayer, name='addPlayer'),
   path('cricket/add/addrecord/', views.addAPlayerRecord, name='addAPlayer'),
   path('cricket/delete/<int:id>', views.cricketdelete, name='delete'),
   path('cricket/update/<int:id>', views.cricketupdate, name='cricketupdate'),
   path('cricket/update/updaterecord/<int:id>', views.cricketupdaterecord, name='cricketupdaterecord')
]
