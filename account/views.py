from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.template import RequestContext
from account.models import *
def view_account(request, account_id):
		account = get_object_or_404(Account, pk=account_id)
		event_list = AccountEvent.objects.filter(account=account_id)
		return render_to_response('account/account.html', {'account': account, 'event_list': event_list}, context_instance=RequestContext(request))

def process_event(request, event_id):
		event = get_object_or_404(AccountEvent, pk=event_id)
		account_id = event.account.id
		if request.POST['action']== 'Edit':
			pass
		elif request.POST['action']== 'Delete':
			event.delete()
		else:
			pass
		
		return HttpResponseRedirect(reverse('account.views.view_account', args=(account_id,)))

def add_event(request, account_id):
		account = get_object_or_404(Account, pk=account_id)
		event = AccountEvent(account_id=account_id, item=request.POST['item'], date=request.POST['date'], income=request.POST['income'], expense=request.POST['expense'], description=request.POST['description'])
		event.save()
		return HttpResponseRedirect(reverse('account.views.view_account', args=(account_id,)))
