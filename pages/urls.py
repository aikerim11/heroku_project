from django.conf.urls import path
from .views import HomePageView

urlpatterns = [
	path('', HomePageView.as_view(), name = 'home'),
	path('about/', AboutPageView.as_view(), name = 'about'),
]