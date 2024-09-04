from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245730',
        'name': 'Nadhif Ryan Alvaro',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)