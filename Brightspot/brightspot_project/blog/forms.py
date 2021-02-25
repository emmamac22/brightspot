from django import forms
from .models import Comment

"""
  Create the forms the site will use. 

  @author Emma Macaluso
  @version February 2021
"""

# Create a form to submit comments. 
class CommentForm(forms.ModelForm):
  # Meta is a container for our data, name and body
  class Meta:
    # get the name and body of a comment
    model = Comment
    fields = ('name', 'body')

    # Represents an HTML input object. Gets the name and body for a comment. 
    widgets = {
      'Name':forms.TextInput(attrs={'class':'form-control'}),
      'body':forms.Textarea(attrs={'class':'form-control'}),  
    }
