from django.urls import path
from . import views
from .views import AddCommentView

"""
  Views of the webpage are mapped to a URL pattern store in the list.

  @author Emma Macaluso
  @version February 2021
"""

# the home page, the about page, and the comment submission page
urlpatterns = [
  path('', views.home, name='blog-home'),
  path('about/', views.about, name='blog-about'),
  path('comment/', AddCommentView.as_view(),  name='add_comment' ),

]

