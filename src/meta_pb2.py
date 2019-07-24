# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meta.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='meta.proto',
  package='ps',
  syntax='proto2',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n\nmeta.proto\x12\x02ps\"l\n\x06PBNode\x12\x0c\n\x04role\x18\x01 \x02(\x05\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x10\n\x08hostname\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\x12\x13\n\x0bis_recovery\x18\x05 \x01(\x08\x12\x13\n\x0b\x63ustomer_id\x18\n \x01(\x05\"Z\n\tPBControl\x12\x0b\n\x03\x63md\x18\x01 \x02(\x05\x12\x18\n\x04node\x18\x02 \x03(\x0b\x32\n.ps.PBNode\x12\x15\n\rbarrier_group\x18\x03 \x01(\x05\x12\x0f\n\x07msg_sig\x18\x04 \x01(\x04\"\xd4\x01\n\x06PBMeta\x12\x0c\n\x04head\x18\x01 \x01(\x05\x12\x0c\n\x04\x62ody\x18\x02 \x01(\x0c\x12\x1e\n\x07\x63ontrol\x18\x03 \x01(\x0b\x32\r.ps.PBControl\x12\x16\n\x07request\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x0e\n\x06\x61pp_id\x18\x07 \x01(\x05\x12\x11\n\ttimestamp\x18\x08 \x01(\x05\x12\x15\n\tdata_type\x18\t \x03(\x05\x42\x02\x10\x01\x12\x13\n\x0b\x63ustomer_id\x18\n \x01(\x05\x12\x0c\n\x04push\x18\x05 \x01(\x08\x12\x19\n\nsimple_app\x18\x06 \x01(\x08:\x05\x66\x61lseB\x02H\x03')
)




_PBNODE = _descriptor.Descriptor(
  name='PBNode',
  full_name='ps.PBNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='ps.PBNode.role', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='ps.PBNode.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='ps.PBNode.hostname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='ps.PBNode.port', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_recovery', full_name='ps.PBNode.is_recovery', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='ps.PBNode.customer_id', index=5,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=126,
)


_PBCONTROL = _descriptor.Descriptor(
  name='PBControl',
  full_name='ps.PBControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='ps.PBControl.cmd', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node', full_name='ps.PBControl.node', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='barrier_group', full_name='ps.PBControl.barrier_group', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg_sig', full_name='ps.PBControl.msg_sig', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=218,
)


_PBMETA = _descriptor.Descriptor(
  name='PBMeta',
  full_name='ps.PBMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='head', full_name='ps.PBMeta.head', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='ps.PBMeta.body', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='control', full_name='ps.PBMeta.control', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request', full_name='ps.PBMeta.request', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='ps.PBMeta.app_id', index=4,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ps.PBMeta.timestamp', index=5,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='ps.PBMeta.data_type', index=6,
      number=9, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='ps.PBMeta.customer_id', index=7,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='push', full_name='ps.PBMeta.push', index=8,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='simple_app', full_name='ps.PBMeta.simple_app', index=9,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=221,
  serialized_end=433,
)

_PBCONTROL.fields_by_name['node'].message_type = _PBNODE
_PBMETA.fields_by_name['control'].message_type = _PBCONTROL
DESCRIPTOR.message_types_by_name['PBNode'] = _PBNODE
DESCRIPTOR.message_types_by_name['PBControl'] = _PBCONTROL
DESCRIPTOR.message_types_by_name['PBMeta'] = _PBMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PBNode = _reflection.GeneratedProtocolMessageType('PBNode', (_message.Message,), dict(
  DESCRIPTOR = _PBNODE,
  __module__ = 'meta_pb2'
  # @@protoc_insertion_point(class_scope:ps.PBNode)
  ))
_sym_db.RegisterMessage(PBNode)

PBControl = _reflection.GeneratedProtocolMessageType('PBControl', (_message.Message,), dict(
  DESCRIPTOR = _PBCONTROL,
  __module__ = 'meta_pb2'
  # @@protoc_insertion_point(class_scope:ps.PBControl)
  ))
_sym_db.RegisterMessage(PBControl)

PBMeta = _reflection.GeneratedProtocolMessageType('PBMeta', (_message.Message,), dict(
  DESCRIPTOR = _PBMETA,
  __module__ = 'meta_pb2'
  # @@protoc_insertion_point(class_scope:ps.PBMeta)
  ))
_sym_db.RegisterMessage(PBMeta)


DESCRIPTOR._options = None
_PBMETA.fields_by_name['data_type']._options = None
# @@protoc_insertion_point(module_scope)
