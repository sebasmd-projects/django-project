from django.shortcuts import render
from django.utils. translation import gettext as _
from . import models
from django.views import generic

class AboutModelListView(generic.ListView):
    context_object_name = 'ctx_about'
    template_name='page/index/index.html'

    def get_queryset(self):
        return models.AboutModel.objects.about_manager()
    