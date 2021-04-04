from django.shortcuts import render
from .models import Title
from django.core.exceptions import ObjectDoesNotExist

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def index(request):
    if request.method == "POST":
       #logger sret massages v console
        logger.info('Post received!')

        title = request.POST["title"]
        logger.info(title)

        try:
            result = Title.objects.get(name=title)
            logger.info(result)
            
        except ObjectDoesNotExist:
            result = "Not found"
            logger.info(result)
        
        return render(request, 'app/index.html', {'retitle': result})

    return render(request, 'app/index.html')
