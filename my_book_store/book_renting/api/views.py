from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import mixins,generics
from book_renting.api.serializers import BookSerializer,RentingSerializer
from book_renting.models import book,renting
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
class view_book(APIView):
    permission_classes=[IsAuthenticated] 
    def get(self,request):
       # books=book.objects.all()
       
        queryset = book.objects.all()
        serialzer=BookSerializer(queryset,many=True)
        return Response(serializer.data)
       # return Response(serializer.data)
   
class add_book(APIView):
    permission_classes=[IsAuthenticated] 
    def post(self,request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class rented_book(APIView):
    permission_classes=[IsAuthenticated] 
    def get(self,request):
        rented_books=renting.objects.all()
        serializer=RentingSerializer(rented_books,many=True)
        return Response(serializer.data)
class rented_book_using_book(APIView):
    pass
class rented_book_using_email(APIView):
    permission_classes=[IsAuthenticated] 
    def get(self,request,emailid):
        book_rented_by_email=renting.objects.filter(email_id=emailid).values()
        print(book_rented_by_email)
        s=RentingSerializer(data=request.data)
        if s.is_valid():
            return Response(s.data)
        return Response(s.errors)
class search_books(APIView):
    permission_classes=[IsAuthenticated] 
    def get(self,request,bookname):
        books=book.objects.filter(title=bookname)
        print(request.GET.urlencode())
        serializer=BookSerializer(books,many=True)
        #print(serializer.data[0]['instance'])
        return Response(serializer.data)
class rent_book(APIView):
    permission_classes=[IsAuthenticated] 
    def post(self,request):
        instances=book.objects.get(id=request.data['renting_book'])
        print(instances.instance)
        if(instances.instance>=1):
             serializer=RentingSerializer(data=request.data)
             if serializer.is_valid(): 
                serializer.save()
             instances.instance = instances.instance-1
             book.save(instances,update_fields=['instance'])
             return Response({"Success": "msb blablabla"}, status=status.HTTP_201_CREATED)
        else:
            return Response (serializer.errros)
        
        
        return Response({"not available ":" 0 books available"})


        

        
    
        




   