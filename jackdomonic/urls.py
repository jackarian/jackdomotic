# from django.contrib import admin
from django.urls import include, path
from control.admin import admin_site


urlpatterns = [
    path('control/', include('control.urls')),
    path('myadmin/', admin_site.urls),
]
