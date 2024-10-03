import re
import datetime
from django.db import models
from libraries.models import Library

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="authors/%Y/%m/%d/")
    libraries = models.ForeignKey(Library, on_delete=models.CASCADE, related_name="Authors")

    def clean(self):
        if self.name:
            self.name = self.name.strip()
            self.name = re.sub(r"([^a-zA-Z0-9_\-. ]+)", "", self.name)
            self.name = self.name.title()

    def __str__(self):
        return self.name