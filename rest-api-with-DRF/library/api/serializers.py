from rest_framework import serializers
from .models import Book, Review


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author"]


class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    book = BookSerializer(read_only=True)
    book_id = serializers.IntegerField(write_only=True)
    comment = serializers.CharField()
    rating = serializers.IntegerField(min_value=1, max_value=5)

    def create(self, validated_data):
        print(validated_data)
        book_id = validated_data.pop("book_id")
        try:
            book = Book.objects.get(id=int(book_id))
        except Book.DoesNotExist:
            raise serializers.ValidationError(
                {"book": "Book with this ID does not exist."}
            )
        return Review.objects.create(book=book, **validated_data)

    def update(self, instance, validated_data):
        instance.book_id = validated_data.get("book_id", instance.book_id)
        instance.comment = validated_data.get("comment", instance.comment)
        instance.rating = validated_data.get("rating", instance.rating)
        instance.save()
        return instance


# class ReviewSerializer(serializers.ModelSerializer):
#     book = BookSerializer(read_only=True)
#     book_id = serializers.IntegerField(write_only=True)

#     class Meta:
#         model = Review
#         fields = ["id", "book", "book_id", "comment", "rating"]

#     def create(self, validated_data):
#         book_id = validated_data.pop("book_id")
#         try:
#             book = Book.objects.get(id=int(book_id))
#         except Book.DoesNotExist:
#             raise serializers.ValidationError(
#                 {"book": "Book with this ID does not exist."}
#             )
#         return Review.objects.create(book=book, **validated_data)

#     def update(self, instance, validated_data):
#         instance.book_id = validated_data.get("book_id", instance.book_id)
#         instance.comment = validated_data.get("comment", instance.comment)
#         instance.rating = validated_data.get("rating", instance.rating)
#         instance.save()
#         return instance
