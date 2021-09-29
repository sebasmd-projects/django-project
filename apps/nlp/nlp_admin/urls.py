from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from . import views

app_name = "nlp_app"

urlpatterns = [
    path(
        _('nlp-panel/'),
        views.IndexPanelView.as_view(), 
        name='nlp-dashboard',
    ),
]
