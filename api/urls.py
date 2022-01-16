from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import ConversationViewSet,ChatViewSet


router = DefaultRouter()
router.register('conversations', ConversationViewSet)
router.register('chats', ChatViewSet)

urlpatterns = [
    path('', include(router.urls))
]
