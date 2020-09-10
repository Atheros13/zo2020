from django.urls import path, include

from app.views.hub import HubView

urls_hub = [
    
    path('', HubView.as_view(), name='hub-home'),

]
