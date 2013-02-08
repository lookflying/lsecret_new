from saving_plan.models import *
from django.contrib import admin
class SavingPlanAdmin(admin.ModelAdmin):
		fields = ['name', 'cost', 'due']
		list_display = ('name', 'cost', 'due', 'create_time')
#		list_filter = ['create_time', 'due']
admin.site.register(SavingPlan, SavingPlanAdmin)

class SavingProgressAdmin(admin.ModelAdmin):
		fields = ['plan', 'money']
		list_display = ('money', 'date')
admin.site.register(SavingProgress, SavingProgressAdmin)
