from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from api.models import Store, Operator, Client


User = get_user_model()
class BaseAPITestCase(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username = 'peter123',
            password = 'peter123'
        )

        self.user2 = User.objects.create_user(
            username = 'paul123',
            password = 'paul123'
        )

        self.user3 = User.objects.create_user(
            username = 'phill123',
            password = 'phill123'
        )

        self.store1 = Store.objects.create(
            name = 'KFC',
            timezone = 'Africa/Kampala',
            phone_number = '+123123345'
        )

        self.store2 = Store.objects.create(
            name = 'Apple',
            timezone = 'Africa/Kampala',
            phone_number = '+123123345'
        )

        self.client1 = Client.objects.create(
            user = self.user1,
            timezone = 'Africa/Kampala',
            phone_number = '+123123345'
        )

        self.client2 = Client.objects.create(
            user = self.user2,
            timezone = 'Africa/Kampala',
            phone_number = '+123123345'
        )

        self.operator1 = Operator.objects.create(
            user = self.user3,
            operator_group = 'A'
        )
