from api.models import Conversation
from rest_framework import status

from api.tests import BaseAPITestCase


class ConversationsAPITestCase(BaseAPITestCase):

    def test_create_conversation(self):
        data = {
            "store_id": self.store1.id,
            "operator_id": self.operator1.id,
            "client_id": self.client1.id
        }
        response = self.client.post('/api/conversations/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_conversation(self):
        conversation = Conversation.objects.create(
            store=self.store2,
            operator=self.operator1,
            client=self.client2
        )
        response = self.client.get(f'/api/conversations/{conversation.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_non_existing_conversation(self):
        response = self.client.get('/api/conversations/10/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
