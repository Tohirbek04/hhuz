from django.urls import path

from apps.views import VacancyListCreateAPIView, VacancyRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('vacancy/', VacancyListCreateAPIView.as_view()),
    path('vacancy/<int:pk>', VacancyRetrieveUpdateDestroyAPIView.as_view())
]
