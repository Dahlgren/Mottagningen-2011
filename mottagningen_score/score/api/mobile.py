from datetime import date as system_date

from piston.handler import BaseHandler
from piston.utils import rc, throttle

from score.models import *

class GroupsHandler(BaseHandler):
    allowed_methods = ('GET')
    
    def read(self, request):
        groupsInfo = {}
        groups = Group.objects.all()
        for g in groups:
            groupsInfo[str(g.id)] = g.name
            
        return {
            'info': [{'status': 0}],
            'groups': groupsInfo
        }
        
class DaysHandler(BaseHandler):
    allowed_methods = ('GET')

    def read(self, request):
        daysInfo = {}
        days = Day.objects.filter(date__lte=int(system_date.today().isoformat().replace('-', '')))
        for d in days:
            daysInfo[d.date] = d.name

        return {
            'info': [{'status': 0}],
            'days': daysInfo
        }

class PostScoreHandler(BaseHandler):
    allowed_methods = ('GET')

    def read(self, request):
        key = request.GET.get('key', '')
        try:
            auth = Key.objects.get(key=key)
        except ObjectDoesNotExist:
            return {'info': [{'status': 1}]}

        if auth != None:
            group = request.GET.get('group', '')
            day = request.GET.get('day', '')
            score = request.GET.get('score', '')
            comment = request.GET.get('comment', '')

            s = Score(group=Group.objects.get(id=group), 
                      day=Day.objects.get(date=day),
                      score=score,
                      comment=comment,
                      author=auth)
            s.save()
            return {'info': [{'status': 0}]}
        else:
            return {'info': [{'status': 1}]}