from django.db.utils import IntegrityError
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from api.models import Chat, Conversation
from api.serializers import ChatSerializer, ConversationSerializer


class ConversationViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response({
                "message": "Failed, non existing Operator or client or store"
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class ChatViewSet(mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
