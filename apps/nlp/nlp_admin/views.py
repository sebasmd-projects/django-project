from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
)


class IndexPanelView(LoginRequiredMixin, TemplateView):
    template_name = "nlp/pages/index.html"
    login_url = reverse_lazy('users_app:user-login')