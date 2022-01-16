from datetime import datetime
from rest_framework import serializers

from api.models import Chat, Conversation, Discount, Schedule


class ChatSerializer(serializers.ModelSerializer):
    conversation_id = serializers.IntegerField(label='conversation')
    discount_id = serializers.IntegerField(label='discount')
    payload = serializers.RegexField('^[a-zA-Z0-9\\s}{\\$%_\\/~@#$%\\^&.)(!?-]*$')

    class Meta:
        model = Chat
        read_only_fields = ['id']
        fields = read_only_fields + [
            'payload',
            'conversation_id',
            'created_date',
            'status',
            'discount_id']

    def create(self, validated_data):
        # updated payload
        payload_input = validated_data.pop('payload')
        conversation_id = validated_data.get('conversation_id')
        discount_id = validated_data.get('discount_id')
        payload = self.populate_payload(payload_input, conversation_id, discount_id)
        chat = Chat.objects.create(**validated_data, payload=payload)
        # Create schedule
        Schedule.objects.create(
            chat=chat,
            sending_date=datetime.now()
        )
        return chat

    @staticmethod
    def populate_payload(payload_input, conversation_id, discount_id):
        try:
            conv = Conversation.objects.select_related(
                'client', 'operator').get(id=conversation_id)
            client_first_name = conv.client.user.first_name
            operator_fullname = f'{conv.operator.user.first_name} ' + f'{conv.operator.user.last_name}'
            discount_code = Discount.objects.get(id=discount_id).discount_code
            payload = payload_input.replace("{{ operator.user.full_name }}", operator_fullname)
            payload = payload.replace("{{ client.user.first_name }}", client_first_name)
            payload = payload.replace("{{ discount.discount_code }}", discount_code)
            return payload
        except (Conversation.DoesNotExist, Discount.DoesNotExist):
            raise serializers.ValidationError('Invalid Conversation or Discount')


class ConversationSerializer(serializers.ModelSerializer):
    store_id = serializers.IntegerField(label='store')
    operator_id = serializers.IntegerField(label='operator')
    client_id = serializers.IntegerField(label='client')
    operator_group = serializers.ReadOnlyField(source='operator.operator_group')
    chats = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        read_only_fields = ['id']
        fields = [
            'store_id',
            'operator_id',
            'operator_group',
            'client_id',
            'status',
            'chats'
        ] + read_only_fields

    def get_chats(self, obj):
        chats = Chat.objects.filter(conversation=obj)
        return ChatSerializer(chats, many=True).data
