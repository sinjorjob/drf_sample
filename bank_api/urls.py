from django.contrib import admin
from django.urls import path, include
from appv1.urls import router as bank_api_router  #add


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(bank_api_router.urls)),  #add
]
