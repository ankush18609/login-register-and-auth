from rest_framework import serializers
from book_renting.models import book,renting

class RentingSerializer(serializers.ModelSerializer):
    class Meta:
        model=renting
        fields='__all__'
class BookSerializer(serializers.ModelSerializer):
      rented_books=RentingSerializer(read_only=True,many=True)
      class Meta:
        model=book
        fields='__all__'
        depth=1