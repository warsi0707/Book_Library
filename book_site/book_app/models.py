from django.db import models

# Create your models here.

class Book(models.Model):
    book_member_name = models.CharField(max_length=200)
    book_name =models.CharField(max_length=50)
    charge = models.IntegerField(help_text="enter price")
    transiction = models.IntegerField(help_text="enter the book want to Issue")
    
# this will show the book name inside the page
    def __str__(self):
        return self. book_member_name
