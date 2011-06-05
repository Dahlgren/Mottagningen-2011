from piston.handler import BaseHandler
from piston.utils import rc, throttle

from django.core.exceptions import ObjectDoesNotExist

from score.models import *

class ScoreHandler(BaseHandler):
    allowed_methods = ('GET')
        
    def read(self, request, nr=0):
        score = []
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
                score.append({d.name: dayInfo})      
        else:
            groups = Group.objects.all()
            day = Day.objects.get(number=nr)
            dayInfo = []
            for g in groups:
                dayInfo.append({
                    g.name: g.score(day)
                })
            score.append({day.name: dayInfo})
            
        return {
            'score': score
        }
        
class PostScoreHandler(BaseHandler):
    allowed_methods = ('GET')
    
    def read(self, request):
        key = request.GET.get('key', '')
        try:
            auth = Key.objects.get(key=key) != None
        except ObjectDoesNotExist:
            return {'info': [{'status': 1}]}
        
        if auth:
            group = request.GET.get('group', '')
            day = request.GET.get('day', '')
            score = request.GET.get('score', '')
            comment = request.GET.get('comment', '')
            
            s = Score(group=Group.objects.get(number=group), 
                      day=Day.objects.get(number=day),
                      score=score,
                      comment=comment)
            s.save()
            return {'info': [{'status': 0}]}
        else:
            return {'info': [{'status': 1}]}
        
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
        
class DaysHandler(BaseHandler):
    allowed_methods = ('GET')

    def read(self, request):
        daysInfo = []
        days = Day.objects.all()
        for d in days:
            daysInfo.append({
            'id': d.number,
            'day': d.name
            })

        return {
            'info': [{'status': 0}],
            'days': daysInfo
        }
        