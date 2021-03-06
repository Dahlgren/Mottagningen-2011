from datetime import date as system_date

from piston.handler import BaseHandler
from piston.utils import rc, throttle

from django.core.exceptions import ObjectDoesNotExist

from score.models import *

def currentDate():
    return int(system_date.today().isoformat().replace('-', ''))

class ScoreHandler(BaseHandler):
    allowed_methods = ('GET')
        
    def read(self, request, date="0"):
        score = {}
        if (date == "0"):
            groups = Group.objects.all()
            days_unchecked = Day.objects.filter(date__lt=currentDate()).order_by('date')
            days = []
            for d in days_unchecked: 
                if len(Score.objects.filter(day=d)) > 0:
                    days.append(d)
            for g in groups:
                groupInfo = []
                for d in days:
                    groupInfo.append(d.score(g))
                score[g.id] = {g.name: groupInfo}  
        else:
            groups = Group.objects.all()
            days = Day.objects.filter(date=date)
            for g in groups:
                groupInfo = []
                for d in days:
                    groupInfo.append(g.score(d))
                score[g.name] = groupInfo
        
        daysInfo = {}
        days_unchecked = Day.objects.filter(date__lt=currentDate()).order_by('date')
        days = []
        for d in days_unchecked: 
            if len(Score.objects.filter(day=d)) > 0:
                days.append(d)
        for d in days:
            daysInfo[d.date] = d.name
            
        return {
            'days': daysInfo,
            'score': score
        }

class GroupHandler(BaseHandler):
    allowed_methods = ('GET')
    
    def read(self, request, id):
        score = {}
        authors = {}
        scores = Score.objects.filter(group=id, registered=True)
        
        for s in scores:
            author = s.author.name
            if(author not in authors):
                authors[author] = s.author.color
            if(author in score):
                score[author] += s.score
            else:
                score[author] = s.score
        
        return {
            'color': authors,
            'score': score
        }
    
        