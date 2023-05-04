from django.db import models
# Create your models here.
class book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    instance=models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
class renting(models.Model):
    renting_date=models.DateField(auto_now=False, auto_now_add=False)
    due_date=models.DateField(auto_now=False, auto_now_add=False)
    email_id=models.EmailField(max_length=254)
    renting_book=models.ForeignKey(book,on_delete=models.CASCADE,related_name='rented_books')
    renting_status=models.BooleanField(default=True)
    def __str__(self):
        return self.renting_book.title
    

