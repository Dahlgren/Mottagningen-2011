from piston.handler import BaseHandler
from piston.utils import rc, throttle

from django.core.exceptions import ObjectDoesNotExist

from score.models import *

class ScoreHandler(BaseHandler):
    allowed_methods = ('GET')
        
    def read(self, request, nr=0):
        points = []
        if (nr == "0"):
            groups = Group.objects.all()
            days = Day.objects.all()
            for d in days:
                dayInfo = []
                dayInfo.append({'id': d.number})
                for g in groups:
                    dayInfo.append({
                        g.name: d.score(g)
                    })
                points.append({d.name: dayInfo})      
        else:
            groups = Group.objects.all()
            day = Day.objects.get(number=nr)
            dayInfo = []
            for g in groups:
                dayInfo.append({
                    g.name: g.score(day)
                })
            points.append({day.name: dayInfo})
            
        return {
            'points': points
        }
        
class PostScoreHandler(BaseHandler):
    allowed_methods = ('GET')
    
    def read(self, request):
        # , key, id, activity, score, comment
        key = request.GET.get('key', '')
        try:
            auth = Key.objects.get(key=key) != None
        except ObjectDoesNotExist:
            return "LOL"
        
        if auth:
            return "OK"
        else:
            return "LOL"
        
class GroupsHandler(BaseHandler):
    allowed_methods = ('GET')
    
    def read(self, request):
        groupsInfo = []
        groups = Group.objects.all()
        for g in groups:
            groupsInfo.append({
                'id': g.number,
                'group': g.name
            })
            
        return {
            'info': [{'status': 0}],
            'groups': groupsInfo
        }
        