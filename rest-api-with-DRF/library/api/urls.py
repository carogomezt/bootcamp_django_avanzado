from django.urls import path
from .views import (
    BookListCreateView,
    BookDetailView,
    ReviewDetailView,
    ReviewListCreateView,
)

urlpatterns = [
    path("books/", BookListCreateView.as_view()),
    path("books/<int:id>/", BookDetailView.as_view()),
    path("reviews/", ReviewListCreateView.as_view()),
    path("reviews/<int:id>/", ReviewDetailView.as_view()),
]
