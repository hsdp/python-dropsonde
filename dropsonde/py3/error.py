from protobuf3.message import Message
from protobuf3.fields import StringField, Int32Field


class Error(Message):
    pass

Error.add_field('source', StringField(field_number=1, required=True))
Error.add_field('code', Int32Field(field_number=2, required=True))
Error.add_field('message', StringField(field_number=3, required=True))
