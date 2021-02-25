from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

"""
  Create the models which will get added as tables into the database. 

  @author Emma Macaluso
  @version February 2021
"""

# Comment class allows anyone to comment on a post
class Comment(models.Model):
  # Create the name, body, and date added fields of the table
  name = models.CharField(max_length=255)
  body = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True) 

  # simple tostring method
  def __str__(self):
    return 'Comment by - %s' % (self.name)

