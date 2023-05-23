from django.urls import path
from .views import helloWorldPageView

urlpatterns = [
    path('', helloWorldPageView, name='helloWord')
]
