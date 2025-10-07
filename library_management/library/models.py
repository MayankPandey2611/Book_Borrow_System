from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    status = models.BooleanField(default=True)  
    added_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)      

    def __str__(self):
        return self.title

class BorrowedBook(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    borrow_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)  # Available or not
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.username} borrowed {self.book.title}"
