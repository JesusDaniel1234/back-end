from .views import QChat10QuestionViewSet, QChat10ResponseViewSet
from rest_framework.routers import SimpleRouter

routes = SimpleRouter()

routes.register("qchat10_questions", QChat10QuestionViewSet)

routes.register("qchat10_responses", QChat10ResponseViewSet)

app_name = "qchat10"

urlpatterns = routes.urls
