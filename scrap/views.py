from django.http import HttpResponse
from scrappers import sachinbansal

def index(request):
    a = sachinbansal.bansal_scrap()[0]
    return HttpResponse("Hello, world. You're at the polls index."+ a["url"]+"<br>"+a["title"]+"<br>"+a["desc"])