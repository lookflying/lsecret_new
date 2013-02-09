from django.http import HttpResponse, HttpResponseRedirect
from saving_plan.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.template import RequestContext

def index(request):
		plan_list = SavingPlan.objects.all()
		return render_to_response('saving_plan/index.html', {'plan_list': plan_list})

def detail(request, plan_id):
		plan = get_object_or_404(SavingPlan, pk=plan_id)
		if plan.last_calc_time <= plan.last_progress_time:
			calc_saved_money(plan)
		progress_list = SavingProgress.objects.filter(plan=plan_id)
		return render_to_response('saving_plan/detail.html', {'plan': plan, 'progress_list': progress_list}, context_instance=RequestContext(request))
	
def calc_saved_money(plan):
		progress_list = SavingProgress.objects.filter(plan=plan.id)
		saved_money = 0
		for progress in progress_list:
			saved_money += progress.money
		plan.saved_money = saved_money
		plan.last_calc_time = timezone.now()
		plan.save()
		return saved_money
	
def add_progress(request, plan_id):
		plan = get_object_or_404(SavingPlan, pk=plan_id)
		plan.last_progress_time = timezone.now()
		plan.save()
		progress = SavingProgress(plan_id=plan_id, money=request.POST['money'])
		progress.save();
		return HttpResponseRedirect(reverse('saving_plan.views.detail', args=(plan_id,)))

