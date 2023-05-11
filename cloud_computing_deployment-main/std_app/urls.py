from django import urls
from django.urls import path
from . views import denied_access_report, denied_access_return, std_books_search_veiw, borrow_book_view
app_name = "std_app"
urlpatterns = [
    path("<int:std_number>/",std_books_search_veiw ,name = "std search"),
    path("<int:std_number>/borrow/<int:bk_id>/",borrow_book_view, name = "student borrow book"),
    path("<int:std_number>/return/<int:bk_id>",denied_access_return,name = "denied access"),
    path("<int:std_number>/borrowed_books_report/",denied_access_report,name = "denied access"),
    path("<int:std_number>/add_book/",denied_access_report,name = "denied access"),
]