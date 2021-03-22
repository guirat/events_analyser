from django.contrib import admin
from django.urls import path
from api.views import EventApiView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", EventApiView.as_view(), name="event"),
]
