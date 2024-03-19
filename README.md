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
    BOOK_TITLE=models.CharField(max_length=30);
    YEAR_OF_PUBLISH=models.DateField();
    AUTHOR_NAME=models.CharField(max_length=20);
    NO_OF_PAGES=models.IntegerField();
    BOOK_PRICE=models.IntegerField();
class BOOKDBAdmin(admin.ModelAdmin):
    list_display=("BOOK_TITLE","YEAR_OF_PUBLISH","AUTHOR_NAME"," BOOK_PRICE","  NO_OF_PAGES");

Admin.py

from django.contrib import admin
from .models import BOOKDB,BOOKAdmin 
admin.site.register(BOOKDB,BOOKAdmin)
```
## OUTPUT

![Table ](https://github.com/KMSusindhar/ORM/assets/155904197/ace0dee7-9920-46e0-8d52-a78b26f08f6a)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
