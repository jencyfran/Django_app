from django.db import models

# Location model to represent a location

class Location(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name

# Item model to represent an item

class Item(models.Model):
    Name = models.CharField(max_length=150)
    date_added = models.DateField(auto_now_add=True)
    Location = models.ForeignKey(Location, on_delete=models.CASCADE)

    
# String representation of the item
    def __str__(self):
        return self.Name
