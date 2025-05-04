# from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

# from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


# Create your views here.
class BookListCreateView(APIView):
    # class BookListCreateView(GenericAPIView):
    #     pagination_class = PageNumberPagination
    #     pagination_class.page_size = 1

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(
            {"status": "success", "data": serializer.data}, status=status.HTTP_200_OK
        )
        # return self.get_paginated_response(
        #     {"status": "success", "data": self.paginate_queryset(serializer.data)}
        # )

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"status": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class BookDetailView(APIView):
    def get_object(self, id):
        try:
            return Book.objects.get(id=id)
        except Book.DoesNotExist:
            return None

    def get(self, request, id):
        book = self.get_object(id)
        if not book:
            return Response(
                {"status": "error", "data": "Not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = BookSerializer(book)
        return Response(
            {"status": "success", "data": serializer.data}, status=status.HTTP_200_OK
        )

    def put(self, request, id):
        book = self.get_object(id)
        if not book:
            return Response(
                {"status": "error", "data": "Not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"status": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, id):
        book = self.get_object(id)
        if not book:
            return Response(
                {"status": "error", "data": "Not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        book.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )
