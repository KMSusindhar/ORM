# Ex02 Django ORM Web Application
## Date: 04/03/2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![image](https://github.com/KMSusindhar/ORM/assets/155904197/47ff541c-9182-4357-8298-07f39589c086)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
Models.py

from django.db import models
from django.contrib import admin
class Books(models.Model):
    title=models.CharField(max_length=30);
    year_of_publishing=models.DateField();
    author_name=models.CharField(max_length=20);
    no_of_pages=models.IntegerField();
    book_price=models.IntegerField();
class BooksAdmin(admin.ModelAdmin):
    list_display=("title","year_of_publishing","author_name","no_of_pages","book_price");

Admin.py

from django.contrib import admin
from .models import Books,BooksAdmin 
admin.site.register(Books,BooksAdmin)
```
## OUTPUT

![Table ](https://github.com/KMSusindhar/ORM/assets/155904197/ace0dee7-9920-46e0-8d52-a78b26f08f6a)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
