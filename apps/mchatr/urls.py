from rest_framework.routers import SimpleRouter
from .views import MChatRResponsesViewSet, MchatRQuestionsViewSet

app_name = "mchatr"

router = SimpleRouter()
router.register(r"mchat_questions", MchatRQuestionsViewSet)
router.register(r"mchat_responses", MChatRResponsesViewSet)

urlpatterns = router.urls
