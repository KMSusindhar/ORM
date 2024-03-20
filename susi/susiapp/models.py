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


