from django.contrib import admin
from django.urls import include, path

from chwideukapp.views import ChwideukRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/chwideuk/', ChwideukRouter.as_view())
]