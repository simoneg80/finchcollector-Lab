from django.db import models

# Create your models here.
class Finch(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  population = models.IntegerField()
  
  # Chaning this instance method to a string method
  # This does not impact the database, therefor no migration is needed
  def __str__(self):
    return f'{self.name} ({self.id})'