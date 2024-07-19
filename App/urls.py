from django.urls import path
from .views import home,books,records,add_author,add_book,add_record,export_records,export_author_records,export_book_records

urlpatterns = [
    path('',home,name='home'),
    path('books',books,name='books'),
    path('records',records,name='records'),
    path('add_book',add_book,name='add book'),
    path('add_author',add_author,name='add-author'),
    path('add_record',add_record,name='add record'),
    path('export_records',export_records,name='export records'),
    path('export_book_records',export_book_records,name='book records'),
    path('export_author_records',export_author_records,name='author records'),
]