from django.http import HttpResponse, HttpResponseRedirect
from saving_plan.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.template import RequestContext

def index(request):
		plan_list = SavingPlan.objects.all()
		return render_to_response('saving_plan/index.html', {'plan_list': plan_list}, context_instance=RequestContext(request))

def detail(request, plan_id):
		plan = get_object_or_404(SavingPlan, pk=plan_id)
		plan.calc_saved_money()
		progress_list = SavingProgress.objects.filter(plan=plan_id)
		return render_to_response('saving_plan/detail.html', {'plan': plan, 'progress_list': progress_list}, context_instance=RequestContext(request))
	
def add_plan(request):
		plan = SavingPlan(name=request.POST['name'], cost=request.POST['cost'], due=request.POST['due'])
		plan.save()
		return HttpResponseRedirect(reverse('saving_plan.views.index', args=()))
	
def add_progress(request, plan_id):
		plan = get_object_or_404(SavingPlan, pk=plan_id)
		plan.last_progress_time = timezone.now()
		plan.save()
		progress = SavingProgress(plan_id=plan_id, money=request.POST['money'])
		progress.save()
		return HttpResponseRedirect(reverse('saving_plan.views.detail', args=(plan_id,)))

def delete_progress(request, plan_id, progress_id):
		plan = get_object_or_404(SavingPlan, pk=plan_id)
		progress = get_object_or_404(SavingProgress, pk=progress_id)
		progress.delete()
		plan.last_progress_time = timezone.now()
		plan.save()
		return HttpResponseRedirect(reverse('saving_plan.views.detail', args=(plan_id,)))

	
def delete_plan(request, plan_id):
		plan = get_object_or_404(SavingPlan, pk=plan_id)
		progress_list = SavingProgress.objects.filter(plan=plan_id)
		for p in progress_list:
				p.delete()
		plan.delete()
		return HttpResponseRedirect(reverse('saving_plan.views.index', args=()))
