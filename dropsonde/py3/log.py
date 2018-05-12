from protobuf3.message import Message
from protobuf3.fields import StringField, Int64Field, BytesField, EnumField
from enum import Enum


class LogMessage(Message):

    class MessageType(Enum):
        OUT = 1
        ERR = 2

LogMessage.add_field('message', BytesField(field_number=1, required=True))
LogMessage.add_field('message_type', EnumField(field_number=2, required=True, enum_cls=LogMessage.MessageType))
LogMessage.add_field('timestamp', Int64Field(field_number=3, required=True))
LogMessage.add_field('app_id', StringField(field_number=4, optional=True))
LogMessage.add_field('source_type', StringField(field_number=5, optional=True))
LogMessage.add_field('source_instance', StringField(field_number=6, optional=True))
