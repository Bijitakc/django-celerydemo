from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forcelery/',include(('forcelery.urls','forcelery'), namespace="forcelery")),
    path('email/',include(('emailapp.urls','emailapp'), namespace="emailapp"))
]
