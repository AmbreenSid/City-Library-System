import re
from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    year_opened = models.PositiveIntegerField(default=datetime.date.today().year, validators=[MinValueValidator(1900), MaxValueValidator(datetime.date.today().year)])
    
    def clean(self):
        if self.name:
            self.name = self.name.strip()
            self.name = re.sub(r"([^a-zA-Z0-9\-. ]+)","",self.name)
            self.name = self.name.title()
        
        if self.address:
            self.address = self.address.strip()

    def __str__(self):
        return self.name
