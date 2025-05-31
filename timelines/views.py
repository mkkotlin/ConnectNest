from django.shortcuts import render

# Create your views here.
def timeline(request):
    return render(request, 'timelines/timeline.html')