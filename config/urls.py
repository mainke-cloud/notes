from django.contrib import admin
from django.urls import path, include
from notes.views import index, add, edit, delete

urlpatterns = [
    path("",index, name="notes-index"),
    path("add/",add, name="notes-add"),
    path("edit/<int:id>",edit, name="notes-edit"),
    path("delete/<int:id>",delete, name="notes-delete"),
    path('oidc/', include('mozilla_django_oidc.urls')),
    path('admin/', admin.site.urls),
]
