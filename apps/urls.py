from django.urls import path

from apps.views import VacancyListCreateAPIView, VacancyRetrieveUpdateDestroyAPIView, LoginAPIView, CustomTokenAPIView

urlpatterns = [
    path('vacancy/', VacancyListCreateAPIView.as_view()),
    path('vacancy/<int:pk>', VacancyRetrieveUpdateDestroyAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('send_code/', CustomTokenAPIView.as_view()),
]
