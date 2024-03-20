# Ex02 Django ORM Web Application
## Date: 04/03/2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![alt text](<Screenshot 2024-03-19 221808.png>)

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
class BOOK(models.Model):
    BOOK_TITLE=models.CharField(max_length=30);
    YEAR_OF_PUBLISH=models.DateField();
    AUTHOR_NAME=models.CharField(max_length=20);
    NO_OF_PAGE=models.IntegerField();
    BOOK_PRICE=models.IntegerField();
class BOOKAdmin(admin.ModelAdmin):
    list_display=("BOOK_TITLE","YEAR_OF_PUBLISH","AUTHOR_NAME","BOOK_PRICE","NO_OF_PAGE");


ADMIN.PY

from django.contrib import admin
from .models import BOOK,BOOKAdmin 
admin.site.register(BOOK,BOOKAdmin)

```
## OUTPUT

![alt text](<Screenshot 2024-03-20 200210-1.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
