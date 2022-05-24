from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls')),
    path('profiles/', include('profiles_api.urls')),
    path('biotools/', include('biotools.urls')),
    path('admin/', admin.site.urls),
]
