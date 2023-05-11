from django import urls
from django.urls import path
from . views import add_book_veiw, return_book_veiw, find_book_view,report_view,borrow_book_view

app_name = "libralian"
urlpatterns = [
    path("<int:admin_id>/",find_book_view, name = "find book url"),
    path("<int:admin_id>/return/<int:bk_id>/",return_book_veiw, name = "return_book_url"),
    path("<int:admin_id>/add_book/",add_book_veiw, name = "denied"),
    path("<int:admin_id>/borrowed_books_report/", report_view, name = "borrowed books report view"),
    path("<int:std_number>/borrow/<int:bk_id>/",borrow_book_view, name = "Denied_access"),
]