
from django.shortcuts import render_to_response, RequestContext

from urlerator.forms import UrlCheckerForm

def home(request):
    url_form = UrlCheckerForm(request.POST or None)

        
    if request.POST:
        address = request.POST['address'] #it gets the post data by Name
        
        print address
        url_output = 'https://maps.google.com/maps?ie=UTF-8&gl=us&daddr=%s&f=d&fb=1&dirflg=d' %(address)
        html_output = "<a href='%s'>Directions</a>" %(url_output)
        if url_form.is_valid():
            form1 = url_form.save(commit=False)
            form1.from_address = address
            form1.url_output = url_output
            form1.save()
            print form1.id
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))