from django.shortcuts import render, HttpResponse

# Create your views here.
def user_main_page(request):
    context = {
        'title':'register',
    }
    return render(request, 'users/index.html', context)
