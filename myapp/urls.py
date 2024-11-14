# myapp/urls.py
from django.urls import path
from .views import login_view, logout_view, signup_view
from . import views

urlpatterns = [
    path('', login_view, name='login'), 
      path('book-list/',views.book_list , name='book_list'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('book/<int:id>/', views.book_detail, name='book_detail'), 
    path('book/new/', views.book_create, name='book_create'),  
    path('book/<int:id>/edit/', views.book_update, name='book_update'),  
    path('book/<int:id>/delete/', views.book_delete, name='book_delete'), 
]
