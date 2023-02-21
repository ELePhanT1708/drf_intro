from django.urls import path

from .views import WomenAPIView

urlpatterns = [
    path('womenlist/', WomenAPIView.as_view()),
    path('womenlist/<int:pk>/', WomenAPIView.as_view()),


]