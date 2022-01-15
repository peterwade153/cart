from rest_framework import serializers

from api.models import Chat, Conversation


class ChatSerializer(serializers.ModelSerializer):
    conversation_id = serializers.IntegerField(label='conversation')
    payload = serializers.RegexField('^[a-zA-Z0-9{}$%_-\/~@#$%^&()!?]$')

    class Meta:
        model = Chat
        read_only_fields = ['id']
        fields = ['payload', 'conversation_id', 'created_date', 'status']

    def validate_payload(self, value):
        # TODO Add validation for payload.
        pass



class ConversationSerializer(serializers.ModelSerializer):
    store_id = serializers.IntegerField(label='store')
    operator_id = serializers.IntegerField(label='operator')
    client_id = serializers.IntegerField(label='client')
    operator_group = serializers.ReadOnlyField(source='operator.operator_group')
    chats = serializers.SerializerMethodField()
    
    class Meta:
        model = Conversation
        read_only_fields = ['id', 'status']
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
