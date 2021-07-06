from django.urls import path, include
from django.contrib import admin

urlpatterns = [
   # url(r'^admin/', admin.site.urls),
    path('admin/',admin.site.urls),
    path('',include('course.urls')),
    
]
