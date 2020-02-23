from django.shortcuts import render

posts = [
    {
        'author': 'MichaelAmaya',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 23, 2020'
    },
    {
        'author': 'BenjaminBenitez',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 20, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
