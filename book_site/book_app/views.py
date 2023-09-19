from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Book

# Create your views here.

def helloView(request):
    books = Book.objects.all()
    return render(request, "viewbook.html" , {"books":books})

def addBookView(request):
    return render(request, "add_book.html")

def addBook(request):
    if request.method=="POST":
        mn=request.POST["book_member_name"]
        bn=request.POST["book_name"]
        c=request.POST["charge"]
        t=request.POST["transiction"]

        print(mn, bn, c, t )

        book=Book()
        book. book_member_name = mn
        book.book_name = bn
        book.charge = c
        book.transiction = t
        book.save()
        return HttpResponseRedirect('/')


def editBook(request):
      if request.method=="POST":
        mn=request.POST["book_member_name"]
        bn=request.POST["book_name"]
        c=request.POST["charge"]
        t=request.POST["transiction"]
        
        book=Book.objects.get(id=request.POST['bookid'])
        book. book_member_name = mn
        book.book_name = bn
        book.charge = c
        book.transiction = t
        book.save()
        return HttpResponseRedirect('/')

def editBookView(request):
    book=Book.objects.get(id=request.GET["bookid"])
  
    return render (request, "editbook.html", {"book":book})


def deleteBookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect('/')
