from django.db import models

class Key(models.Model):
    key = models.CharField(max_length = 30)
    name = models.CharField(max_length = 30)
    
    def __unicode__(self):
        return self.name

class Group(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length = 30)
    
    def score(self, day):
        sum = 0
        scores = Score.objects.filter(group=self, day=day)
        for s in scores:
            if s.registered:
                sum += s.score
        return sum
    
    def __unicode__(self):
        return self.name

class Day(models.Model):
    date = models.IntegerField()
    name = models.CharField(max_length = 100)
    
    def score(self, group):
        sum = 0
        scores = Score.objects.filter(group=group, day__date__lte=self.date)
        for s in scores:
            if s.registered:
                sum += s.score
        return sum
        
    def __unicode__(self):
        return self.name
    
class Score(models.Model):
    day = models.ForeignKey(Day)
    group = models.ForeignKey(Group)
    score = models.FloatField()
    registered = models.BooleanField(default=False)
    comment = models.CharField(max_length = 300, null=True, blank=True)
    author = models.ForeignKey(Key)
    
    def __unicode__(self):
        return self.day.__unicode__() + " - " + self.group.__unicode__() + " - " + str(self.score) + " - " + self.author.__unicode__()