# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from score.models import *

@login_required(login_url='/login/')
def admin(request):
    if request.method == 'GET':
        registered = []
        days = Day.objects.all()
        for d in days:
            registered.append({d: Score.objects.filter(day=d, registered=True)})
        unregistered = Score.objects.filter(registered=False)
        return render(request, 'admin.html', {'registered': registered, 'unregistered': unregistered})
    elif request.method == 'POST':
        scores = request.POST.get('scores')
        for s in scores:
            score = Score.objects.get(id=s)
            score.registered = True
            score.save()
            
        return redirect('/score/admin')
        
    