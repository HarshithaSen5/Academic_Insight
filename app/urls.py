from django.urls import path
from .views import StudView

urlpatterns = [
    path("", StudView.as_view(), name="stud"),
]