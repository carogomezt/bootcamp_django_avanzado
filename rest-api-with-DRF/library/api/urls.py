from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    path("books/", BookListCreateView.as_view()),
    path("books/<int:id>/", BookDetailView.as_view()),
]
