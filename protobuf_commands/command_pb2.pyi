# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from typing import Optional as typing___Optional
from typing import Text as typing___Text

from google.protobuf.descriptor import \
    Descriptor as google___protobuf___descriptor___Descriptor
from google.protobuf.descriptor import \
    FileDescriptor as google___protobuf___descriptor___FileDescriptor
from google.protobuf.message import \
    Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class Command(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name: typing___Text = ...
    data: builtin___bytes = ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        data : typing___Optional[builtin___bytes] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"data",b"data",u"name",b"name"]) -> None: ...
type___Command = Command
