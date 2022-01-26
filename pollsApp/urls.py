from django.urls import path, include

from pollsApp.views import poll_view

urlpatterns = [
    path('viewPoll/', poll_view, name='poll_view'),
]
