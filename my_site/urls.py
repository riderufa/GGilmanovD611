"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from p_library import views
from p_library.views import AuthorEdit, AuthorList, FriendList,  author_create_many, books_authors_create_many, friend_detail, FriendEdit, BookEdit

app_name = 'p_library'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index, name='index_books'),
    path('leasing/', views.leasing, name='leasing_books'),
    path('publishing/', views.index_publishing, name='publishing_books'),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('leasing/leasing_book/', views.leasing_book),
    path('leasing/unleasing_book/', views.unleasing_book),
    path('author/create', AuthorEdit.as_view(), name='author_create'),  
    path('authors', AuthorList.as_view(), name='author_list'),  
    path('friends', FriendList.as_view(), name='friend_list'),  
    path('friend/create', FriendEdit.as_view(), name='friend_create'),  
    path('book/create', BookEdit.as_view(), name='book_create'),  
    path('friend/<str:f_n>', friend_detail, name='friend_detail_url'),
    path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)