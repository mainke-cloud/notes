from django.contrib import admin
from django.urls import path, include
from notes.views import index

urlpatterns = [
    path("",index, name="notes-index"),
    path('oidc/', include('mozilla_django_oidc.urls')),
    path('admin/', admin.site.urls),
]
