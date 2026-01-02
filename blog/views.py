from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'John Doe',
        'title': 'First Post',
        'content': 'This is the content of the first post.',
        'date_posted': 'April 20, 2024'},
    {
        'author': 'Jane Smith', 
        'title': 'Second Post',
        'content': 'This is the content of the second post.',
        'date_posted': 'April 21, 2024'},
]

# Create your views here.

def home(request):
  context = {'posts': posts}
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})