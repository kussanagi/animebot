from django.shortcuts import render
from .models import Title
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    if request.method == "POST":
        title = request.POST["title"]
        try:
            result = Title.objects.get(name=title)
            
        except ObjectDoesNotExist:
            result = "Not found"
        
            return render(request, 'orange/index.html', {'retitle': result})
        
        return render(request, 'orange/index.html', {'retitle': result})

    return render(request, 'orange/index.html')
