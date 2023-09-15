# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: datadriven.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='datadriven.proto',
  package='datadriven',
  syntax='proto3',
  serialized_options=b'\n\033io.grpc.examples.datadrivenB\017DataDrivenProtoP\001\242\002\003HLW',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x64\x61tadriven.proto\x12\ndatadriven\"\x1e\n\x0bReadRequest\x12\x0f\n\x07request\x18\x01 \x01(\t\"\x1c\n\tReadReply\x12\x0f\n\x07message\x18\x01 \x01(\t2L\n\nTextReader\x12>\n\x08ReadText\x12\x17.datadriven.ReadRequest\x1a\x15.datadriven.ReadReply\"\x00\x30\x01\x42\x36\n\x1bio.grpc.examples.datadrivenB\x0f\x44\x61taDrivenProtoP\x01\xa2\x02\x03HLWb\x06proto3'
)




_READREQUEST = _descriptor.Descriptor(
  name='ReadRequest',
  full_name='datadriven.ReadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='datadriven.ReadRequest.request', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=62,
)


_READREPLY = _descriptor.Descriptor(
  name='ReadReply',
  full_name='datadriven.ReadReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='datadriven.ReadReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=92,
)

DESCRIPTOR.message_types_by_name['ReadRequest'] = _READREQUEST
DESCRIPTOR.message_types_by_name['ReadReply'] = _READREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReadRequest = _reflection.GeneratedProtocolMessageType('ReadRequest', (_message.Message,), {
  'DESCRIPTOR' : _READREQUEST,
  '__module__' : 'datadriven_pb2'
  # @@protoc_insertion_point(class_scope:datadriven.ReadRequest)
  })
_sym_db.RegisterMessage(ReadRequest)

ReadReply = _reflection.GeneratedProtocolMessageType('ReadReply', (_message.Message,), {
  'DESCRIPTOR' : _READREPLY,
  '__module__' : 'datadriven_pb2'
  # @@protoc_insertion_point(class_scope:datadriven.ReadReply)
  })
_sym_db.RegisterMessage(ReadReply)


DESCRIPTOR._options = None

_TEXTREADER = _descriptor.ServiceDescriptor(
  name='TextReader',
  full_name='datadriven.TextReader',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=94,
  serialized_end=170,
  methods=[
  _descriptor.MethodDescriptor(
    name='ReadText',
    full_name='datadriven.TextReader.ReadText',
    index=0,
    containing_service=None,
    input_type=_READREQUEST,
    output_type=_READREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEXTREADER)

DESCRIPTOR.services_by_name['TextReader'] = _TEXTREADER

# @@protoc_insertion_point(module_scope)