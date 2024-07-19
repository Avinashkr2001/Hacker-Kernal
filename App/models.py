from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    bio=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    published_date=models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class BorrowRecord(models.Model):
    user_name=models.CharField(max_length=50)
    borrow_date=models.CharField(max_length=100)
    return_date=models.CharField(max_length=100)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    def __str__(self):
        return self.user_name
    
