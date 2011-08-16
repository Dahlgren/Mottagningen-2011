from datetime import date as system_date

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from score.models import *

def currentDate():
    return int(system_date.today().isoformat().replace('-', ''))

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
        scores = int(request.POST.get('scores'))
        for s in scores:
            score = Score.objects.get(pk=s)
            score.registered = True
            score.save()
            
        return redirect('/score/admin')
        
def demo(request):
    div_height = request.GET.get('h')
    if not div_height: div_height = "600"
    
    div_width = request.GET.get('w')
    if not div_width: div_width = "1000"
    
    if request.method == 'GET':
        return render(request, 'demo.html', {'div_height': div_height, 'div_width': div_width})
        
def graph(request):
    if request.method == 'GET':
        graph = request.GET.get('graph_div')
        if not graph: graph = "graph"
        
        group = request.GET.get('group_div')
        if not group: group = "group"
        
        return render(request, 'graph.js', {'graph_div': graph, 
                                            'group_div': group})      
    