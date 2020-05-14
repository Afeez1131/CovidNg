
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('', include('state.urls')),
    path('', include('total.urls'))
   # path('total', include('total.urls'))
]


handler404 = 'homepage.views.error_404_view'