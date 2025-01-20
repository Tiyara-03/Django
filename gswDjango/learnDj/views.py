from django.shortcuts import render

# Create your views here.
def all_learnDj(request):
    return render(request, 'learnDj/all_learnDj.html')
