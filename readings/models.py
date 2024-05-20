from django.db import models

class Date_time(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    

class Book(Date_time):
    title = models.CharField(max_length=255, null=False, blank=False)
    author = models.CharField(max_length=255, null=False, blank=False)
    genre = models.CharField(max_length=100, blank=True)
    published_year = models.IntegerField(blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True)
    pages = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    cover_image_url = models.CharField(max_length=255, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return "Titulo: " + self.title + "Autor: " + self.author 