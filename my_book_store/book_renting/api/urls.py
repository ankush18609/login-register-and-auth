from django.contrib import admin
from django.urls import path,include
from book_renting.api import urls
from . import views
app_name='Book_renting'
urlpatterns=[
    path('add',views.add_book.as_view(),name='add'),
    path('rent/view_all',views.rented_book.as_view(),name='rent'),
    path('view',views.view_book.as_view(),name='view'),
    path('search/<str:bookname>',views.search_books.as_view(),name='search'),
    path('rent/rent_a_book',views.rent_book.as_view(),name='renting'),
    path('rent/email/<str:emailid>',views.rented_book_using_email.as_view(),name='emailsearch')
]
