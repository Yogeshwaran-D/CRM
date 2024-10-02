from django.urls import path
from .views import LeadListView ,LeadDetailView, LeadCreateView ,LeadsUpdateView ,LeadsDeleteView
app_name="leads"
urlpatterns = [
    path("",LeadListView.as_view(),name="leads-list"),
    path("create/",LeadCreateView.as_view(),name="leads-create"),
    path("<int:pk>/",LeadDetailView.as_view(),name="leads-details"),
    path("<int:pk>/update/",LeadsUpdateView.as_view(),name="leads-update"),
    path("<int:pk>/delete/",LeadsDeleteView.as_view(),name="leads-delete"),
]
