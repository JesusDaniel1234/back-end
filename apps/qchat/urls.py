from django.urls import path
from .views import QChatQuestionViewSet, QChatResponseViewSet
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register("", QChatQuestionViewSet)
route.register("", QChatResponseViewSet)

app_name = "qchat"

urlpatterns = route.urls
