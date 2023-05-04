from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import mixins,generics
from book_renting.api.serializers import BookSerializer,RentingSerializer
from book_renting.models import book,renting
class view_book(APIView):
    def get(self,request):
        books=book.objects.all()
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data)
   
class add_book(APIView):
    def post(self,request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class rented_book(APIView):
    def get(self,request):
        rented_books=renting.objects.all()
        serializer=RentingSerializer(rented_books,many=True)
        return Response(serializer.data)
class rented_book_using_book(APIView):
    pass
class rented_book_using_email(APIView):
    pass
class search_books(APIView):
    def get(self,request,bookname):
        books=book.objects.filter(title=bookname)
        serializer=BookSerializer(books,many=True)
        print(serializer.data[0]['instance'])
        return Response(serializer.data[0]['instance'])
class rent_book(APIView):
    def post(self,request):
        instances=book.objects.get(id=request.data['renting_book'])
        print(instances.instance)
        
        serializer=RentingSerializer(data=request.data)
        #print(serializer)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        



   