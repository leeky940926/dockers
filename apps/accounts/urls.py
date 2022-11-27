from django.urls import path
from accounts.views import SigUpView

urlpatterns = [
    path("signup", SigUpView.as_view())
]

