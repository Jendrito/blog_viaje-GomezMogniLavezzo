from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contacto.urls')),
    path('', include('experiencias.urls')),
    path('', include('tramites.urls'))
]