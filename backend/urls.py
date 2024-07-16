
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token # for login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('app/', include('apps.urls')),
    path('auth/', obtain_auth_token), # for login
]

