from rest_framework.serializers import ModelSerializer
from Nested_Serializers_App.models import Author ,Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    books_by_author = BookSerializer(
        read_only=True, many=True )     #   add this line for Nested Serializer effect.

    class Meta:
        model = Author
        fields = '__all__'




