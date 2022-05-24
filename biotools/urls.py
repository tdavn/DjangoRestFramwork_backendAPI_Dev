from django.urls import path
from .views import HomeView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='biotools_idx'),
    path('seq/', views.seq, name='seq_info')
]
