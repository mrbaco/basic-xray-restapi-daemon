# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proxy/socks/config.proto
# Protobuf Python Version: 5.27.2
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
    'proxy/socks/config.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xray_rpc.common.net import address_pb2 as common_dot_net_dot_address__pb2
from xray_rpc.common.protocol import server_spec_pb2 as common_dot_protocol_dot_server__spec__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18proxy/socks/config.proto\x12\x10xray.proxy.socks\x1a\x18\x63ommon/net/address.proto\x1a!common/protocol/server_spec.proto\"-\n\x07\x41\x63\x63ount\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x85\x02\n\x0cServerConfig\x12-\n\tauth_type\x18\x01 \x01(\x0e\x32\x1a.xray.proxy.socks.AuthType\x12>\n\x08\x61\x63\x63ounts\x18\x02 \x03(\x0b\x32,.xray.proxy.socks.ServerConfig.AccountsEntry\x12,\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x1b.xray.common.net.IPOrDomain\x12\x13\n\x0budp_enabled\x18\x04 \x01(\x08\x12\x12\n\nuser_level\x18\x06 \x01(\r\x1a/\n\rAccountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"D\n\x0c\x43lientConfig\x12\x34\n\x06server\x18\x01 \x03(\x0b\x32$.xray.common.protocol.ServerEndpoint*%\n\x08\x41uthType\x12\x0b\n\x07NO_AUTH\x10\x00\x12\x0c\n\x08PASSWORD\x10\x01\x42R\n\x14\x63om.xray.proxy.socksP\x01Z%github.com/xtls/xray-core/proxy/socks\xaa\x02\x10Xray.Proxy.Socksb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proxy.socks.config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.xray.proxy.socksP\001Z%github.com/xtls/xray-core/proxy/socks\252\002\020Xray.Proxy.Socks'
  _globals['_SERVERCONFIG_ACCOUNTSENTRY']._loaded_options = None
  _globals['_SERVERCONFIG_ACCOUNTSENTRY']._serialized_options = b'8\001'
  _globals['_AUTHTYPE']._serialized_start=488
  _globals['_AUTHTYPE']._serialized_end=525
  _globals['_ACCOUNT']._serialized_start=107
  _globals['_ACCOUNT']._serialized_end=152
  _globals['_SERVERCONFIG']._serialized_start=155
  _globals['_SERVERCONFIG']._serialized_end=416
  _globals['_SERVERCONFIG_ACCOUNTSENTRY']._serialized_start=369
  _globals['_SERVERCONFIG_ACCOUNTSENTRY']._serialized_end=416
  _globals['_CLIENTCONFIG']._serialized_start=418
  _globals['_CLIENTCONFIG']._serialized_end=486
# @@protoc_insertion_point(module_scope)
