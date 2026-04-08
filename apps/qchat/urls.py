from django.urls import path
from .views import QChatQuestionViewSet, QChatResponseViewSet
from rest_framework.routers import SimpleRouter

route = SimpleRouter()

route.register("qchat_questions", QChatQuestionViewSet)

route.register("qchat_responses", QChatResponseViewSet)

app_name = "qchat"

urlpatterns = route.urls
