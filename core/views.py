from django.shortcuts import render

def home(request):
    # import ipdb; ipdb.set_trace()
    ip = request.META['REMOTE_ADDR']
    return render(request, 'core/home.html', {'ip': ip})
