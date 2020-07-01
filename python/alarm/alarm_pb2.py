# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alarm.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='alarm.proto',
  package='com.beerfie.stonest.grpc.showeralarm',
  syntax='proto3',
  serialized_options=b'P\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x61larm.proto\x12$com.beerfie.stonest.grpc.showeralarm\".\n\x05\x41larm\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03\x64\x61y\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\t\"M\n\x0e\x41\x63tionResponse\x12;\n\x06\x61larms\x18\x01 \x03(\x0b\x32+.com.beerfie.stonest.grpc.showeralarm.Alarm\"\x12\n\x10ListAlarmsParams2\xe6\x03\n\nAlarmStore\x12r\n\x0b\x44\x65leteAlarm\x12+.com.beerfie.stonest.grpc.showeralarm.Alarm\x1a\x34.com.beerfie.stonest.grpc.showeralarm.ActionResponse\"\x00\x12r\n\x0bUpdateAlarm\x12+.com.beerfie.stonest.grpc.showeralarm.Alarm\x1a\x34.com.beerfie.stonest.grpc.showeralarm.ActionResponse\"\x00\x12|\n\nListAlarms\x12\x36.com.beerfie.stonest.grpc.showeralarm.ListAlarmsParams\x1a\x34.com.beerfie.stonest.grpc.showeralarm.ActionResponse\"\x00\x12r\n\x0b\x43reateAlarm\x12+.com.beerfie.stonest.grpc.showeralarm.Alarm\x1a\x34.com.beerfie.stonest.grpc.showeralarm.ActionResponse\"\x00\x42\x02P\x01\x62\x06proto3'
)




_ALARM = _descriptor.Descriptor(
  name='Alarm',
  full_name='com.beerfie.stonest.grpc.showeralarm.Alarm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.beerfie.stonest.grpc.showeralarm.Alarm.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='day', full_name='com.beerfie.stonest.grpc.showeralarm.Alarm.day', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='com.beerfie.stonest.grpc.showeralarm.Alarm.time', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=53,
  serialized_end=99,
)


_ACTIONRESPONSE = _descriptor.Descriptor(
  name='ActionResponse',
  full_name='com.beerfie.stonest.grpc.showeralarm.ActionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='alarms', full_name='com.beerfie.stonest.grpc.showeralarm.ActionResponse.alarms', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=101,
  serialized_end=178,
)


_LISTALARMSPARAMS = _descriptor.Descriptor(
  name='ListAlarmsParams',
  full_name='com.beerfie.stonest.grpc.showeralarm.ListAlarmsParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=180,
  serialized_end=198,
)

_ACTIONRESPONSE.fields_by_name['alarms'].message_type = _ALARM
DESCRIPTOR.message_types_by_name['Alarm'] = _ALARM
DESCRIPTOR.message_types_by_name['ActionResponse'] = _ACTIONRESPONSE
DESCRIPTOR.message_types_by_name['ListAlarmsParams'] = _LISTALARMSPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Alarm = _reflection.GeneratedProtocolMessageType('Alarm', (_message.Message,), {
  'DESCRIPTOR' : _ALARM,
  '__module__' : 'alarm_pb2'
  # @@protoc_insertion_point(class_scope:com.beerfie.stonest.grpc.showeralarm.Alarm)
  })
_sym_db.RegisterMessage(Alarm)

ActionResponse = _reflection.GeneratedProtocolMessageType('ActionResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONRESPONSE,
  '__module__' : 'alarm_pb2'
  # @@protoc_insertion_point(class_scope:com.beerfie.stonest.grpc.showeralarm.ActionResponse)
  })
_sym_db.RegisterMessage(ActionResponse)

ListAlarmsParams = _reflection.GeneratedProtocolMessageType('ListAlarmsParams', (_message.Message,), {
  'DESCRIPTOR' : _LISTALARMSPARAMS,
  '__module__' : 'alarm_pb2'
  # @@protoc_insertion_point(class_scope:com.beerfie.stonest.grpc.showeralarm.ListAlarmsParams)
  })
_sym_db.RegisterMessage(ListAlarmsParams)


DESCRIPTOR._options = None

_ALARMSTORE = _descriptor.ServiceDescriptor(
  name='AlarmStore',
  full_name='com.beerfie.stonest.grpc.showeralarm.AlarmStore',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=201,
  serialized_end=687,
  methods=[
  _descriptor.MethodDescriptor(
    name='DeleteAlarm',
    full_name='com.beerfie.stonest.grpc.showeralarm.AlarmStore.DeleteAlarm',
    index=0,
    containing_service=None,
    input_type=_ALARM,
    output_type=_ACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateAlarm',
    full_name='com.beerfie.stonest.grpc.showeralarm.AlarmStore.UpdateAlarm',
    index=1,
    containing_service=None,
    input_type=_ALARM,
    output_type=_ACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListAlarms',
    full_name='com.beerfie.stonest.grpc.showeralarm.AlarmStore.ListAlarms',
    index=2,
    containing_service=None,
    input_type=_LISTALARMSPARAMS,
    output_type=_ACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateAlarm',
    full_name='com.beerfie.stonest.grpc.showeralarm.AlarmStore.CreateAlarm',
    index=3,
    containing_service=None,
    input_type=_ALARM,
    output_type=_ACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ALARMSTORE)

DESCRIPTOR.services_by_name['AlarmStore'] = _ALARMSTORE

# @@protoc_insertion_point(module_scope)
