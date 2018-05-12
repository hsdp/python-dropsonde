from protobuf3.message import Message
from protobuf3.fields import Int64Field, MessageField, Int32Field, StringField, EnumField
from dropsonde.py3.uuid import UUID
from enum import Enum


class HttpStartStop(Message):
    pass


class PeerType(Enum):
    Client = 1
    Server = 2


class Method(Enum):
    GET = 1
    POST = 2
    PUT = 3
    DELETE = 4
    HEAD = 5
    ACL = 6
    BASELINE_CONTROL = 7
    BIND = 8
    CHECKIN = 9
    CHECKOUT = 10
    CONNECT = 11
    COPY = 12
    DEBUG = 13
    LABEL = 14
    LINK = 15
    LOCK = 16
    MERGE = 17
    MKACTIVITY = 18
    MKCALENDAR = 19
    MKCOL = 20
    MKREDIRECTREF = 21
    MKWORKSPACE = 22
    MOVE = 23
    OPTIONS = 24
    ORDERPATCH = 25
    PATCH = 26
    PRI = 27
    PROPFIND = 28
    PROPPATCH = 29
    REBIND = 30
    REPORT = 31
    SEARCH = 32
    SHOWMETHOD = 33
    SPACEJUMP = 34
    TEXTSEARCH = 35
    TRACE = 36
    TRACK = 37
    UNBIND = 38
    UNCHECKOUT = 39
    UNLINK = 40
    UNLOCK = 41
    UPDATE = 42
    UPDATEREDIRECTREF = 43
    VERSION_CONTROL = 44

HttpStartStop.add_field('startTimestamp', Int64Field(field_number=1, required=True))
HttpStartStop.add_field('stopTimestamp', Int64Field(field_number=2, required=True))
HttpStartStop.add_field('requestId', MessageField(field_number=3, required=True, message_cls=UUID))
HttpStartStop.add_field('peerType', EnumField(field_number=4, required=True, enum_cls=PeerType))
HttpStartStop.add_field('method', EnumField(field_number=5, required=True, enum_cls=Method))
HttpStartStop.add_field('uri', StringField(field_number=6, required=True))
HttpStartStop.add_field('remoteAddress', StringField(field_number=7, required=True))
HttpStartStop.add_field('userAgent', StringField(field_number=8, required=True))
HttpStartStop.add_field('statusCode', Int32Field(field_number=9, required=True))
HttpStartStop.add_field('contentLength', Int64Field(field_number=10, required=True))
HttpStartStop.add_field('applicationId', MessageField(field_number=12, optional=True, message_cls=UUID))
HttpStartStop.add_field('instanceIndex', Int32Field(field_number=13, optional=True))
HttpStartStop.add_field('instanceId', StringField(field_number=14, optional=True))
HttpStartStop.add_field('forwarded', StringField(field_number=15, repeated=True))
