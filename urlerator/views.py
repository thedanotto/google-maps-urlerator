
from django.shortcuts import render_to_response, RequestContext

def home(request):
    if request.POST:
        address = request.POST['address'] #it gets the post data by Name
        print address
        google_directions_url = 'https://maps.google.com/maps?ie=UTF-8&gl=us&daddr=%s&f=d&fb=1&dirflg=d' %(address)
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))