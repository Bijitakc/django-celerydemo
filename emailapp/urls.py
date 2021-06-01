from django.urls import path,include
from .views import ReviewEmailView

urlpatterns = [
    path('reviews/',ReviewEmailView.as_view(),name="reviews")
]
