from django.urls import path
from accounts.views import SigUpnView

urlpatterns = [
    path("signup", SigUpnView.as_view())
]

