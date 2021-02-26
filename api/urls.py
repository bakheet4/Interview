from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

urlpatterns = [
    path('countries/', CreateView.as_view(), name="create"),
    path('country/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details")
]