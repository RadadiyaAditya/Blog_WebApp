from django.shortcuts import render

post = [
    {
        'author': 'Aditya Radaiya',
        'title': 'Django framework',
        'content': 'First post content include basic info about django framework',
        'date_posted': '09 December 2024'
    },
    {
        'author': 'Ravi Zala',
        'title': 'Flask framework',
        'content': 'Second post content include basic info about flask framework',
        'date_posted': '10 December 2024'
    }
]
# Create your views here.
def home(request):
    context = {
        'posts': post
    }
    return render(request, 'blog_temp/home.html', context)

def about(request):
    return render(request, 'blog_temp/about.html', {'title':'About'}) 