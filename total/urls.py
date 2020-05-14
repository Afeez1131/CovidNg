from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('confirmed', views.ConfirmedApi)
router.register('active', views.ActiveApi)
router.register('discharged', views.DischargedApi)
router.register('death', views.DeathApi)
router.register('sample', views.SampleApi)
router.register('', views.TotalApi)
#router.register('date', views.TotalDateApi)


urlpatterns = [
	path('total/', include(router.urls)),
]