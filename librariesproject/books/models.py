import re
from django.db import models
from libraries.models import Library
from authors.models import Author

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to = "books/%Y/%m/%d/")
    pages = models.IntegerField()
    genres = models.TextField()      
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    libraries = models.ManyToManyField(Library, blank=True, related_name="books")

    def clean(self):
        if self.name:
            self.name = self.name.strip()
            self.name = re.sub(r"([^a-zA-Z\-. ]+)","",self.name)
            self.name = self.name.title()
        
        if self.genres:
            self.genres = self.genres.strip()
    
    def __str__(self):
        return self.name
