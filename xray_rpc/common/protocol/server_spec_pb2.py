# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: common/protocol/server_spec.proto
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
    'common/protocol/server_spec.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xray_rpc.common.net import address_pb2 as common_dot_net_dot_address__pb2
from xray_rpc.common.protocol import user_pb2 as common_dot_protocol_dot_user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!common/protocol/server_spec.proto\x12\x14xray.common.protocol\x1a\x18\x63ommon/net/address.proto\x1a\x1a\x63ommon/protocol/user.proto\"v\n\x0eServerEndpoint\x12,\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x1b.xray.common.net.IPOrDomain\x12\x0c\n\x04port\x18\x02 \x01(\r\x12(\n\x04user\x18\x03 \x03(\x0b\x32\x1a.xray.common.protocol.UserB^\n\x18\x63om.xray.common.protocolP\x01Z)github.com/xtls/xray-core/common/protocol\xaa\x02\x14Xray.Common.Protocolb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.protocol.server_spec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.xray.common.protocolP\001Z)github.com/xtls/xray-core/common/protocol\252\002\024Xray.Common.Protocol'
  _globals['_SERVERENDPOINT']._serialized_start=113
  _globals['_SERVERENDPOINT']._serialized_end=231
# @@protoc_insertion_point(module_scope)
