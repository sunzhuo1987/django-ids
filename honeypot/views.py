from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from ids.honeypot.forms import TestForm

@login_required
def index(request):
    if request.method == 'POST': 
        form = TestForm(request.POST) 
        if form.is_valid(): 
            return render_to_response('ids/honeypot/index.html', {'form': form,})
		else:
			return render_to_response('ids/honeypot/index.html', {'form': form, 'error',True})
    else:
        form = TestForm()

    return render_to_response('ids/honeypot/index.html', {'form': form,})

    
