from api.models import Chat, Conversation
from rest_framework import status

from api.tests import BaseAPITestCase


class ChatTestCase(BaseAPITestCase):

    def test_get_chats(self):
        conversation = Conversation.objects.create(
            store=self.store2,
            operator=self.operator1,
            client=self.client2
        )
        chat = Chat.objects.create(
            payload='hello jsaon',
            conversation=conversation,
            discount=self.discount,
            status='NEW'
        )
        response = self.client.get(f'/api/chats/{chat.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_non_exisiting_chats(self):
        response = self.client.get('/api/chats/5/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_chat(self):
        conv = Conversation.objects.create(
            store=self.store2,
            operator=self.operator1,
            client=self.client2
        )
        data = {
            "payload": "Hello {{ client.user.first_name }}. This is {{ operator.user.full_name }}.\nHow can I help you?",
            "conversation_id": conv.id,
            "status": "NEW",
            "discount_id": self.discount.id
        }
        response = self.client.post('/api/chats/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_create_chat(self):
        data = {
            "payload": "Hello {{ client.user.first_name }}. This is {{ operator.user.full_name }}.\nHow can I help you?",
            "conversation_id": 2,
            "status": "NEW",
            "discount_id": self.discount.id
        }
        response = self.client.post('/api/chats/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
