from protobuf3.message import Message
from protobuf3.fields import MessageField, StringField, Int64Field, EnumField
from enum import Enum
from dropsonde.py3.http import HttpStartStop
from dropsonde.py3.log import LogMessage
from dropsonde.py3.metric import ContainerMetric, ValueMetric, CounterEvent
from dropsonde.py3.error import Error


class Envelope(Message):

    class EventType(Enum):
        HttpStartStop = 4
        LogMessage = 5
        ValueMetric = 6
        CounterEvent = 7
        Error = 8
        ContainerMetric = 9

    class TagsEntry(Message):
        pass

Envelope.TagsEntry.add_field('key', StringField(field_number=1, optional=True))
Envelope.TagsEntry.add_field('value', StringField(field_number=2, optional=True))
Envelope.add_field('origin', StringField(field_number=1, required=True))
Envelope.add_field('eventType', EnumField(field_number=2, required=True, enum_cls=Envelope.EventType))
Envelope.add_field('timestamp', Int64Field(field_number=6, optional=True))
Envelope.add_field('deployment', StringField(field_number=13, optional=True))
Envelope.add_field('job', StringField(field_number=14, optional=True))
Envelope.add_field('index', StringField(field_number=15, optional=True))
Envelope.add_field('ip', StringField(field_number=16, optional=True))
Envelope.add_field('tags', MessageField(field_number=17, repeated=True, message_cls=Envelope.TagsEntry))
Envelope.add_field('httpStartStop', MessageField(field_number=7, optional=True, message_cls=HttpStartStop))
Envelope.add_field('logMessage', MessageField(field_number=8, optional=True, message_cls=LogMessage))
Envelope.add_field('valueMetric', MessageField(field_number=9, optional=True, message_cls=ValueMetric))
Envelope.add_field('counterEvent', MessageField(field_number=10, optional=True, message_cls=CounterEvent))
Envelope.add_field('error', MessageField(field_number=11, optional=True, message_cls=Error))
Envelope.add_field('containerMetric', MessageField(field_number=12, optional=True, message_cls=ContainerMetric))
