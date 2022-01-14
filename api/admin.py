from django.contrib import admin

from api.models import Store, Discount, Operator, Client, Chat, Conversation

admin.site.register(Store)
admin.site.register(Discount)
admin.site.register(Operator)
admin.site.register(Client)
admin.site.register(Chat)
admin.site.register(Conversation)
