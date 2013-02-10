from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from saving_plan.models import SavingPlan

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lsecret.views.home', name='home'),
    # url(r'^lsecret/', include('lsecret.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
#	url(r'^saving_plan/$',
#		ListView.as_view(
#				model=SavingPlan,
#				context_object_name='plan_list',
#				template_name='saving_plan/index.html')),
	url(r'^saving_plan/$', 'saving_plan.views.index'),
	url(r'^saving_plan/(?P<plan_id>\d+)/$', 'saving_plan.views.detail'),
	url(r'^saving_plan/(?P<plan_id>\d+)/add_progress/$', 'saving_plan.views.add_progress'),
    url(r'^saving_plan/(?P<plan_id>\d+)/delete_progress/(?P<progress_id>\d+)/$', 'saving_plan.views.delete_progress'),
	url(r'^saving_plan/add/', 'saving_plan.views.add_plan'),
	url(r'^saving_plan/(?P<plan_id>\d+)/delete/$', 'saving_plan.views.delete_plan'),
	# Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
