# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dropsonde/py2/uuid.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dropsonde/py2/uuid.proto',
  package='events',
  syntax='proto2',
  serialized_pb=_b('\n\x18\x64ropsonde/py2/uuid.proto\x12\x06\x65vents\"!\n\x04UUID\x12\x0b\n\x03low\x18\x01 \x02(\x04\x12\x0c\n\x04high\x18\x02 \x02(\x04\x42\x30\n!org.cloudfoundry.dropsonde.eventsB\x0bUuidFactory')
)




_UUID = _descriptor.Descriptor(
  name='UUID',
  full_name='events.UUID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='low', full_name='events.UUID.low', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='high', full_name='events.UUID.high', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=69,
)

DESCRIPTOR.message_types_by_name['UUID'] = _UUID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UUID = _reflection.GeneratedProtocolMessageType('UUID', (_message.Message,), dict(
  DESCRIPTOR = _UUID,
  __module__ = 'dropsonde.py2.uuid_pb2'
  # @@protoc_insertion_point(class_scope:events.UUID)
  ))
_sym_db.RegisterMessage(UUID)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!org.cloudfoundry.dropsonde.eventsB\013UuidFactory'))
# @@protoc_insertion_point(module_scope)
