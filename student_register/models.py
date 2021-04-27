from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Student(models.Model):
    fullname = models.CharField(max_length=100)
    issue_date = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=15)
    book_code = models.ForeignKey(Book, on_delete=models.CASCADE)
