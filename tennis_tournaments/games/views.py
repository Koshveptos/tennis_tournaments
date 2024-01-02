from django.shortcuts import render, HttpResponse

# Create your views here.
def games(request):
    context = {
        'title':'live games',
    }
    return render(request, 'games/games.html', context)

