from protobuf3.message import Message
from protobuf3.fields import UInt64Field, StringField, DoubleField, Int32Field


class ValueMetric(Message):
    pass


class CounterEvent(Message):
    pass


class ContainerMetric(Message):
    pass

ValueMetric.add_field('name', StringField(field_number=1, required=True))
ValueMetric.add_field('value', DoubleField(field_number=2, required=True))
ValueMetric.add_field('unit', StringField(field_number=3, required=True))
CounterEvent.add_field('name', StringField(field_number=1, required=True))
CounterEvent.add_field('delta', UInt64Field(field_number=2, required=True))
CounterEvent.add_field('total', UInt64Field(field_number=3, optional=True))
ContainerMetric.add_field('applicationId', StringField(field_number=1, required=True))
ContainerMetric.add_field('instanceIndex', Int32Field(field_number=2, required=True))
ContainerMetric.add_field('cpuPercentage', DoubleField(field_number=3, required=True))
ContainerMetric.add_field('memoryBytes', UInt64Field(field_number=4, required=True))
ContainerMetric.add_field('diskBytes', UInt64Field(field_number=5, required=True))
ContainerMetric.add_field('memoryBytesQuota', UInt64Field(field_number=6, optional=True))
ContainerMetric.add_field('diskBytesQuota', UInt64Field(field_number=7, optional=True))
