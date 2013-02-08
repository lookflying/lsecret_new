from django.db import models
from django.utils import timezone
# Create your models here.
class SavingPlan(models.Model):
		name = models.CharField(max_length=255)
		cost = models.IntegerField()
		create_time = models.DateTimeField("create time", default=timezone.now())
		due = models.DateTimeField('due date')
		saved_money = models.IntegerField(default=0)
		last_progress_time = models.DateTimeField("last progress time", default=timezone.now())
		last_calc_time = models.DateTimeField("last calculate time", default=timezone.now())
		def __unicode__(self):
				return self.name



class SavingProgress(models.Model):
		plan = models.ForeignKey(SavingPlan)
		money = models.IntegerField()
		date = models.DateTimeField('progress date', default=timezone.now())
		def __unicode__(self):
				return "RMB:" + self.money.__str__() + "\t" + self.date.__str__()
