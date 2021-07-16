from django import urls
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    ### add login page
    path('api-auth/', include('rest_framework.urls')),
    path('', include('books.urls')),
]