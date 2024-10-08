# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: app/proxyman/command/command.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'app/proxyman/command/command.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xray_rpc.common.protocol import user_pb2 as common_dot_protocol_dot_user__pb2
from xray_rpc.common.serial import typed_message_pb2 as common_dot_serial_dot_typed__message__pb2
from xray_rpc.core import config_pb2 as core_dot_config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"app/proxyman/command/command.proto\x12\x19xray.app.proxyman.command\x1a\x1a\x63ommon/protocol/user.proto\x1a!common/serial/typed_message.proto\x1a\x11\x63ore/config.proto\"<\n\x10\x41\x64\x64UserOperation\x12(\n\x04user\x18\x01 \x01(\x0b\x32\x1a.xray.common.protocol.User\"$\n\x13RemoveUserOperation\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"E\n\x11\x41\x64\x64InboundRequest\x12\x30\n\x07inbound\x18\x01 \x01(\x0b\x32\x1f.xray.core.InboundHandlerConfig\"\x14\n\x12\x41\x64\x64InboundResponse\"#\n\x14RemoveInboundRequest\x12\x0b\n\x03tag\x18\x01 \x01(\t\"\x17\n\x15RemoveInboundResponse\"W\n\x13\x41lterInboundRequest\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x33\n\toperation\x18\x02 \x01(\x0b\x32 .xray.common.serial.TypedMessage\"\x16\n\x14\x41lterInboundResponse\"H\n\x12\x41\x64\x64OutboundRequest\x12\x32\n\x08outbound\x18\x01 \x01(\x0b\x32 .xray.core.OutboundHandlerConfig\"\x15\n\x13\x41\x64\x64OutboundResponse\"$\n\x15RemoveOutboundRequest\x12\x0b\n\x03tag\x18\x01 \x01(\t\"\x18\n\x16RemoveOutboundResponse\"X\n\x14\x41lterOutboundRequest\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x33\n\toperation\x18\x02 \x01(\x0b\x32 .xray.common.serial.TypedMessage\"\x17\n\x15\x41lterOutboundResponse\"\x08\n\x06\x43onfig2\xc5\x05\n\x0eHandlerService\x12k\n\nAddInbound\x12,.xray.app.proxyman.command.AddInboundRequest\x1a-.xray.app.proxyman.command.AddInboundResponse\"\x00\x12t\n\rRemoveInbound\x12/.xray.app.proxyman.command.RemoveInboundRequest\x1a\x30.xray.app.proxyman.command.RemoveInboundResponse\"\x00\x12q\n\x0c\x41lterInbound\x12..xray.app.proxyman.command.AlterInboundRequest\x1a/.xray.app.proxyman.command.AlterInboundResponse\"\x00\x12n\n\x0b\x41\x64\x64Outbound\x12-.xray.app.proxyman.command.AddOutboundRequest\x1a..xray.app.proxyman.command.AddOutboundResponse\"\x00\x12w\n\x0eRemoveOutbound\x12\x30.xray.app.proxyman.command.RemoveOutboundRequest\x1a\x31.xray.app.proxyman.command.RemoveOutboundResponse\"\x00\x12t\n\rAlterOutbound\x12/.xray.app.proxyman.command.AlterOutboundRequest\x1a\x30.xray.app.proxyman.command.AlterOutboundResponse\"\x00\x42m\n\x1d\x63om.xray.app.proxyman.commandP\x01Z.github.com/xtls/xray-core/app/proxyman/command\xaa\x02\x19Xray.App.Proxyman.Commandb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.proxyman.command.command_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.xray.app.proxyman.commandP\001Z.github.com/xtls/xray-core/app/proxyman/command\252\002\031Xray.App.Proxyman.Command'
  _globals['_ADDUSEROPERATION']._serialized_start=147
  _globals['_ADDUSEROPERATION']._serialized_end=207
  _globals['_REMOVEUSEROPERATION']._serialized_start=209
  _globals['_REMOVEUSEROPERATION']._serialized_end=245
  _globals['_ADDINBOUNDREQUEST']._serialized_start=247
  _globals['_ADDINBOUNDREQUEST']._serialized_end=316
  _globals['_ADDINBOUNDRESPONSE']._serialized_start=318
  _globals['_ADDINBOUNDRESPONSE']._serialized_end=338
  _globals['_REMOVEINBOUNDREQUEST']._serialized_start=340
  _globals['_REMOVEINBOUNDREQUEST']._serialized_end=375
  _globals['_REMOVEINBOUNDRESPONSE']._serialized_start=377
  _globals['_REMOVEINBOUNDRESPONSE']._serialized_end=400
  _globals['_ALTERINBOUNDREQUEST']._serialized_start=402
  _globals['_ALTERINBOUNDREQUEST']._serialized_end=489
  _globals['_ALTERINBOUNDRESPONSE']._serialized_start=491
  _globals['_ALTERINBOUNDRESPONSE']._serialized_end=513
  _globals['_ADDOUTBOUNDREQUEST']._serialized_start=515
  _globals['_ADDOUTBOUNDREQUEST']._serialized_end=587
  _globals['_ADDOUTBOUNDRESPONSE']._serialized_start=589
  _globals['_ADDOUTBOUNDRESPONSE']._serialized_end=610
  _globals['_REMOVEOUTBOUNDREQUEST']._serialized_start=612
  _globals['_REMOVEOUTBOUNDREQUEST']._serialized_end=648
  _globals['_REMOVEOUTBOUNDRESPONSE']._serialized_start=650
  _globals['_REMOVEOUTBOUNDRESPONSE']._serialized_end=674
  _globals['_ALTEROUTBOUNDREQUEST']._serialized_start=676
  _globals['_ALTEROUTBOUNDREQUEST']._serialized_end=764
  _globals['_ALTEROUTBOUNDRESPONSE']._serialized_start=766
  _globals['_ALTEROUTBOUNDRESPONSE']._serialized_end=789
  _globals['_CONFIG']._serialized_start=791
  _globals['_CONFIG']._serialized_end=799
  _globals['_HANDLERSERVICE']._serialized_start=802
  _globals['_HANDLERSERVICE']._serialized_end=1511
# @@protoc_insertion_point(module_scope)
