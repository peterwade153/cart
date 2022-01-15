from rest_framework import serializers

from api.models import Conversation


class ConversationSerializer(serializers.ModelSerializer):
    store_id = serializers.IntegerField(source='store')
    operator_id = serializers.IntegerField(source='operator')
    client_id = serializers.IntegerField(source='client')
    
    class Meta:
        model = Conversation
        read_only_fields = ['id']
        fields = [
            'store_id', 
            'operator_id', 
            # 'operator_group', 
            'client_id', 
            'status',
            # 'chats'
        ] + read_only_fields
