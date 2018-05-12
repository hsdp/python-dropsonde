from protobuf3.message import Message
from protobuf3.fields import UInt64Field


class UUID(Message):
    pass

UUID.add_field('low', UInt64Field(field_number=1, required=True))
UUID.add_field('high', UInt64Field(field_number=2, required=True))
