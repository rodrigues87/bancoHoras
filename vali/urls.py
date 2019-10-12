from django.urls import path
from .views import ValiDashboardView

urlpatterns = [
    path('dashboard/', ValiDashboardView.as_view(), name="dashboard")
]
