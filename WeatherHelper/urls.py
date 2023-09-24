from django.contrib import admin
from django.urls import path, include

import Weather

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Weather.urls'))
]
