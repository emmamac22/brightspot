from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment
from django.views.generic import CreateView
from .forms import CommentForm
from django.urls import reverse_lazy

"""
  Views of the webpage. Views take a web request and return a web response.

  @author Emma Macaluso
  @version February 2021
"""

# Fuction that returns a rendered view of the home page
def home(request):

  # Accesses all comments in the comment databse
  all_comments = Comment.objects.all()

  # Store all comments in a dictionary
  context = {
    'all_comments':all_comments,
  }
  return render(request, 'blog/home.html', context)

# Test method, unused in final product
def about(request):

  # returns a simple html page displaying Blog About
  return HttpResponse('<h1>Blog About</h1>')

# Class to display the comment submission page
class AddCommentView(CreateView):
  # Set model, form, and html template
  model = Comment
  form_class = CommentForm
  template_name = "blog/add_comment.html"

  # On successful creation of a comment, direct user back 
  # to the home page
  success_url = reverse_lazy(home)