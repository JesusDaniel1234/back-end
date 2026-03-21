from rest_framework.routers import DefaultRouter
from .views import MChatRResponsesViewSet, MchatRQuestionsViewSet

app_name = "mchatr"

router = DefaultRouter()
router.register(r"mchat_questions", MchatRQuestionsViewSet)
router.register(r"mchat_responses", MChatRResponsesViewSet)

urlpatterns = router.urls
