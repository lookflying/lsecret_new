from django.db import models
from django.utils import timezone
# Create your models here.
class SavingPlan(models.Model):
		name = models.CharField(max_length=255)
		cost = models.DecimalField(max_digits=20, decimal_places=2, default=0)
		create_time = models.DateTimeField("create time", default=timezone.now())
		due = models.DateField('due date')
		saved_money = models.DecimalField(max_digits=20, decimal_places=2, default=0)
		last_progress_time = models.DateTimeField("last progress time", default=timezone.now())
		last_calc_time = models.DateTimeField("last calculate time", default=timezone.now())

		def __unicode__(self):
				return self.name

		def status(self):
			self.calc_saved_money()
			if self.saved_money >= self.cost:
				return "Completed"
			elif timezone.now() < self.due:
				return "In Progress"
			else:
				return "Over Due"

		def calc_saved_money(self):
			if self.last_calc_time < self.last_progress_time:
				progress_list = SavingProgress.objects.filter(plan=self.id)
				saved_money = 0
				for progress in progress_list:
					saved_money += progress.money
				self.saved_money = saved_money
				self.last_calc_time = timezone.now()
				self.save()

class SavingProgress(models.Model):
		plan = models.ForeignKey(SavingPlan)
		money = models.DecimalField(max_digits=20, decimal_places=2, default=0)
		date = models.DateField('progress date', auto_now=True)
		def __unicode__(self):
				return "RMB:" + self.money.__str__() + "\t" + self.date.__str__()
