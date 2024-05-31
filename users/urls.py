from django.urls import path

from users.views import SignUpAPIView

urlpatterns = [
    path('sign_up/', SignUpAPIView.as_view())
]


