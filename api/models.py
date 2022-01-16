import pytz
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

User = get_user_model()


# Validators
phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message='please enter phonenumber in the format +123123123, upto 15 digits allowed!',
    code='Invalid phone'
)

payload_regex = RegexValidator(
    regex=r'^[a-zA-Z0-9{}$%_-\/~@#$%^&()!?]$',
    message='Payload had invalid characters',
    code='Invalid payload'
)

all_timezones_choices = sorted((item, item) for item in pytz.all_timezones)

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Store(BaseModel):
    name = models.CharField(max_length=50)
    timezone = models.CharField(max_length=32, choices=all_timezones_choices)
    phone_number = models.CharField(validators=[phone_regex], max_length=15)

    def __str__(self):
        return self.name
    

class Discount(BaseModel):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    discount_code = models.CharField(max_length=32)

# Operator group choices
A = 'A'
B = 'B'
operator_group_choices = ((A, 'A'), (B, 'B'))

class Operator(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    operator_group = models.CharField(max_length=10, choices=operator_group_choices)


class Client(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timezone = models.CharField(max_length=32, choices=all_timezones_choices)
    phone_number = models.CharField(validators=[phone_regex], max_length=15)

# Status choices
PENDING = 'PENDING'
RESOLVED = 'RESOLVED'
conversation_choices = ((PENDING, 'PENDING'), (RESOLVED, 'RESOLVED'))

class Conversation(BaseModel):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    status = models.CharField(max_length=32, choices=conversation_choices, default=PENDING)

    def __str__(self) -> str:
        return self.store

# Status choices
NEW = 'NEW'
SENT = 'SENT'
status_choices = ((NEW, 'NEW'), (SENT, 'SENT'))

class Chat(BaseModel):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    payload = models.CharField(max_length=300, validators=[payload_regex])
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    status = models.CharField(max_length=32, choices=status_choices)


class Schedule(BaseModel):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sending_date = models.DateField()

