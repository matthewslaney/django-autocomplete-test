import django

from django.conf.urls import patterns, include, url
from django.views import generic

if django.VERSION < (1, 7):
    import autocomplete_light
    autocomplete_light.autodiscover()

from django.contrib import admin
admin.autodiscover()

try:
    from hvad_autocomplete import urls as hvad
except ImportError:
    # django 1.6 not support by hvad
    hvad = None

from django.conf.urls import patterns, url
from django.views import generic

import autocomplete_light

from .forms import NonAdminAddAnotherModelForm
from .models import NonAdminAddAnotherModel


urlpatterns = patterns('',
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'$', autocomplete_light.CreateView.as_view(
        model=NonAdminAddAnotherModel, form_class=NonAdminAddAnotherModelForm),
        name='non_admin_add_another_model_create'),
    url(r'(?P<pk>\d+)/$', generic.UpdateView.as_view(
        model=NonAdminAddAnotherModel, form_class=NonAdminAddAnotherModelForm),
        name='non_admin_add_another_model_update'),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
