
from django.shortcuts import render_to_response, RequestContext

from urlerator.forms import UrlCheckerForm

def home(request):
    url_form = UrlCheckerForm(request.POST or None)

        
    if request.POST:
        address = request.POST['address'] #it gets the post data by Name
        print address
        google_directions_url = 'https://maps.google.com/maps?ie=UTF-8&gl=us&daddr=%s&f=d&fb=1&dirflg=d' %(address)
        if url_form.is_valid():
            form1 = url_form.save(commit=False)
            form1.from_address = address
            form1.url_output = google_directions_url
            form1.save()
            print form1.id
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))