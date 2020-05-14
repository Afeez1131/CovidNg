from django.urls import path, include
from . import views#, StateDeleteView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('state', views.StateListView)
#router.register('', StateDeleteView.as_view())




urlpatterns = [
	path('', include(router.urls)),
]