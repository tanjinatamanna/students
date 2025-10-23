from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/', include('calculator.urls')),   # <-- add this line
    path('students/', include('students.urls')),
    path('', include('cvbuilder.urls')),
]
   


