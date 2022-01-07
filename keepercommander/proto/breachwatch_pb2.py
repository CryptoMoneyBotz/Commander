# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: breachwatch.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x62reachwatch.proto\x12\x0b\x42reachWatch\"\xa1\x01\n\x18\x42reachWatchRecordRequest\x12\x11\n\trecordUid\x18\x01 \x01(\x0c\x12\x15\n\rencryptedData\x18\x02 \x01(\x0c\x12=\n\x13\x62reachWatchInfoType\x18\x03 \x01(\x0e\x32 .BreachWatch.BreachWatchInfoType\x12\x1c\n\x14updateUserWhoScanned\x18\x04 \x01(\x08\"z\n\x18\x42reachWatchUpdateRequest\x12G\n\x18\x62reachWatchRecordRequest\x18\x01 \x03(\x0b\x32%.BreachWatch.BreachWatchRecordRequest\x12\x15\n\rencryptedData\x18\x02 \x01(\x0c\"L\n\x17\x42reachWatchRecordStatus\x12\x11\n\trecordUid\x18\x01 \x01(\x0c\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x0e\n\x06reason\x18\x03 \x01(\t\"b\n\x19\x42reachWatchUpdateResponse\x12\x45\n\x17\x62reachWatchRecordStatus\x18\x01 \x03(\x0b\x32$.BreachWatch.BreachWatchRecordStatus\"3\n\x17\x42reachWatchTokenRequest\x12\x18\n\x10\x62reachWatchToken\x18\x01 \x01(\x0c\"M\n\x18\x42reachWatchTokenResponse\x12\x18\n\x10\x62reachWatchToken\x18\x01 \x01(\x0c\x12\x17\n\x0f\x63lientEncrypted\x18\x02 \x01(\x08\"Y\n\x17\x41nonymizedTokenResponse\x12\x13\n\x0b\x64omainToken\x18\x01 \x01(\x0c\x12\x12\n\nemailToken\x18\x02 \x01(\x0c\x12\x15\n\rpasswordToken\x18\x03 \x01(\x0c\"(\n\tHashCheck\x12\r\n\x05hash1\x18\x01 \x01(\x0c\x12\x0c\n\x04\x65uid\x18\x02 \x01(\x0c\"s\n\x18\x42reachWatchStatusRequest\x12\x17\n\x0f\x61nonymizedToken\x18\x01 \x01(\x0c\x12)\n\thashCheck\x18\x02 \x03(\x0b\x32\x16.BreachWatch.HashCheck\x12\x13\n\x0bremovedEuid\x18\x03 \x03(\x0c\"A\n\nHashStatus\x12\r\n\x05hash1\x18\x01 \x01(\x0c\x12\x0c\n\x04\x65uid\x18\x02 \x01(\x0c\x12\x16\n\x0e\x62reachDetected\x18\x03 \x01(\x08\"H\n\x19\x42reachWatchStatusResponse\x12+\n\nhashStatus\x18\x02 \x03(\x0b\x32\x17.BreachWatch.HashStatus\"Z\n\x1b\x45nterprisePublicKeyResponse\x12\x1b\n\x13\x65nterprisePublicKey\x18\x01 \x01(\x0c\x12\x1e\n\x16\x65nterpriseECCPublicKey\x18\x02 \x01(\x0c\"&\n\x0f\x46reeScanRequest\x12\x13\n\x0bhashedEmail\x18\x01 \x01(\x0c\"C\n\x10\x46reeScanResponse\x12\x15\n\remailBreaches\x18\x01 \x01(\x05\x12\x18\n\x10passwordBreaches\x18\x02 \x01(\x05\" \n\x0fPaidUserRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"$\n\x10PaidUserResponse\x12\x10\n\x08paidUser\x18\x01 \x01(\x08\"$\n\x13\x44\x65tailedScanRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"\'\n\x16UseOneTimeTokenRequest\x12\r\n\x05token\x18\x01 \x01(\x0c\"g\n\x0b\x42reachEvent\x12\x0c\n\x04site\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x18\n\x10passwordInBreach\x18\x03 \x01(\x08\x12\x0c\n\x04\x64\x61te\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\"\x89\x01\n\x17UseOneTimeTokenResponse\x12\x15\n\remailBreaches\x18\x01 \x01(\x05\x12\x18\n\x10passwordBreaches\x18\x02 \x01(\x05\x12.\n\x0c\x62reachEvents\x18\x03 \x03(\x0b\x32\x18.BreachWatch.BreachEvent\x12\r\n\x05\x65mail\x18\x04 \x01(\t\"-\n\x0fOneTimeUseToken\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0b\n\x03pad\x18\x02 \x01(\t\"1\n\x17\x46reePasswordScanRequest\x12\x16\n\x0ehashedPassword\x18\x01 \x01(\x0c\"4\n\x18\x46reePasswordScanResponse\x12\x18\n\x10passwordBreaches\x18\x01 \x01(\x03*9\n\x13\x42reachWatchInfoType\x12\n\n\x06RECORD\x10\x00\x12\x16\n\x12\x41LTERNATE_PASSWORD\x10\x01\x42\'\n\x18\x63om.keepersecurity.protoB\x0b\x42reachWatchb\x06proto3')

_BREACHWATCHINFOTYPE = DESCRIPTOR.enum_types_by_name['BreachWatchInfoType']
BreachWatchInfoType = enum_type_wrapper.EnumTypeWrapper(_BREACHWATCHINFOTYPE)
RECORD = 0
ALTERNATE_PASSWORD = 1


_BREACHWATCHRECORDREQUEST = DESCRIPTOR.message_types_by_name['BreachWatchRecordRequest']
_BREACHWATCHUPDATEREQUEST = DESCRIPTOR.message_types_by_name['BreachWatchUpdateRequest']
_BREACHWATCHRECORDSTATUS = DESCRIPTOR.message_types_by_name['BreachWatchRecordStatus']
_BREACHWATCHUPDATERESPONSE = DESCRIPTOR.message_types_by_name['BreachWatchUpdateResponse']
_BREACHWATCHTOKENREQUEST = DESCRIPTOR.message_types_by_name['BreachWatchTokenRequest']
_BREACHWATCHTOKENRESPONSE = DESCRIPTOR.message_types_by_name['BreachWatchTokenResponse']
_ANONYMIZEDTOKENRESPONSE = DESCRIPTOR.message_types_by_name['AnonymizedTokenResponse']
_HASHCHECK = DESCRIPTOR.message_types_by_name['HashCheck']
_BREACHWATCHSTATUSREQUEST = DESCRIPTOR.message_types_by_name['BreachWatchStatusRequest']
_HASHSTATUS = DESCRIPTOR.message_types_by_name['HashStatus']
_BREACHWATCHSTATUSRESPONSE = DESCRIPTOR.message_types_by_name['BreachWatchStatusResponse']
_ENTERPRISEPUBLICKEYRESPONSE = DESCRIPTOR.message_types_by_name['EnterprisePublicKeyResponse']
_FREESCANREQUEST = DESCRIPTOR.message_types_by_name['FreeScanRequest']
_FREESCANRESPONSE = DESCRIPTOR.message_types_by_name['FreeScanResponse']
_PAIDUSERREQUEST = DESCRIPTOR.message_types_by_name['PaidUserRequest']
_PAIDUSERRESPONSE = DESCRIPTOR.message_types_by_name['PaidUserResponse']
_DETAILEDSCANREQUEST = DESCRIPTOR.message_types_by_name['DetailedScanRequest']
_USEONETIMETOKENREQUEST = DESCRIPTOR.message_types_by_name['UseOneTimeTokenRequest']
_BREACHEVENT = DESCRIPTOR.message_types_by_name['BreachEvent']
_USEONETIMETOKENRESPONSE = DESCRIPTOR.message_types_by_name['UseOneTimeTokenResponse']
_ONETIMEUSETOKEN = DESCRIPTOR.message_types_by_name['OneTimeUseToken']
_FREEPASSWORDSCANREQUEST = DESCRIPTOR.message_types_by_name['FreePasswordScanRequest']
_FREEPASSWORDSCANRESPONSE = DESCRIPTOR.message_types_by_name['FreePasswordScanResponse']
BreachWatchRecordRequest = _reflection.GeneratedProtocolMessageType('BreachWatchRecordRequest', (_message.Message,), {
  'DESCRIPTOR' : _BREACHWATCHRECORDREQUEST,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.BreachWatchRecordRequest)
  })
_sym_db.RegisterMessage(BreachWatchRecordRequest)

BreachWatchUpdateRequest = _reflection.GeneratedProtocolMessageType('BreachWatchUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _BREACHWATCHUPDATEREQUEST,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.BreachWatchUpdateRequest)
  })
_sym_db.RegisterMessage(BreachWatchUpdateRequest)

BreachWatchRecordStatus = _reflection.GeneratedProtocolMessageType('BreachWatchRecordStatus', (_message.Message,), {
  'DESCRIPTOR' : _BREACHWATCHRECORDSTATUS,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.BreachWatchRecordStatus)
  })
_sym_db.RegisterMessage(BreachWatchRecordStatus)

BreachWatchUpdateResponse = _reflection.GeneratedProtocolMessageType('BreachWatchUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _BREACHWATCHUPDATERESPONSE,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.BreachWatchUpdateResponse)
  })
_sym_db.RegisterMessage(BreachWatchUpdateResponse)

BreachWatchTokenRequest = _reflection.GeneratedProtocolMessageType('BreachWatchTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _BREACHWATCHTOKENREQUEST,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.BreachWatchTokenRequest)
  })
_sym_db.RegisterMessage(BreachWatchTokenRequest)

BreachWatchTokenResponse = _reflection.GeneratedProtocolMessageType('BreachWatchTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _BREACHWATCHTOKENRESPONSE,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.BreachWatchTokenResponse)
  })
_sym_db.RegisterMessage(BreachWatchTokenResponse)

AnonymizedTokenResponse = _reflection.GeneratedProtocolMessageType('AnonymizedTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _ANONYMIZEDTOKENRESPONSE,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.AnonymizedTokenResponse)
  })
_sym_db.RegisterMessage(AnonymizedTokenResponse)

HashCheck = _reflection.GeneratedProtocolMessageType('HashCheck', (_message.Message,), {
  'DESCRIPTOR' : _HASHCHECK,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.HashCheck)
  })
_sym_db.RegisterMessage(HashCheck)

BreachWatchStatusRequest = _reflection.GeneratedProtocolMessageType('BreachWatchStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _BREACHWATCHSTATUSREQUEST,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.BreachWatchStatusRequest)
  })
_sym_db.RegisterMessage(BreachWatchStatusRequest)

HashStatus = _reflection.GeneratedProtocolMessageType('HashStatus', (_message.Message,), {
  'DESCRIPTOR' : _HASHSTATUS,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.HashStatus)
  })
_sym_db.RegisterMessage(HashStatus)

BreachWatchStatusResponse = _reflection.GeneratedProtocolMessageType('BreachWatchStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _BREACHWATCHSTATUSRESPONSE,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.BreachWatchStatusResponse)
  })
_sym_db.RegisterMessage(BreachWatchStatusResponse)

EnterprisePublicKeyResponse = _reflection.GeneratedProtocolMessageType('EnterprisePublicKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _ENTERPRISEPUBLICKEYRESPONSE,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.EnterprisePublicKeyResponse)
  })
_sym_db.RegisterMessage(EnterprisePublicKeyResponse)

FreeScanRequest = _reflection.GeneratedProtocolMessageType('FreeScanRequest', (_message.Message,), {
  'DESCRIPTOR' : _FREESCANREQUEST,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.FreeScanRequest)
  })
_sym_db.RegisterMessage(FreeScanRequest)

FreeScanResponse = _reflection.GeneratedProtocolMessageType('FreeScanResponse', (_message.Message,), {
  'DESCRIPTOR' : _FREESCANRESPONSE,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.FreeScanResponse)
  })
_sym_db.RegisterMessage(FreeScanResponse)

PaidUserRequest = _reflection.GeneratedProtocolMessageType('PaidUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _PAIDUSERREQUEST,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.PaidUserRequest)
  })
_sym_db.RegisterMessage(PaidUserRequest)

PaidUserResponse = _reflection.GeneratedProtocolMessageType('PaidUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _PAIDUSERRESPONSE,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.PaidUserResponse)
  })
_sym_db.RegisterMessage(PaidUserResponse)

DetailedScanRequest = _reflection.GeneratedProtocolMessageType('DetailedScanRequest', (_message.Message,), {
  'DESCRIPTOR' : _DETAILEDSCANREQUEST,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.DetailedScanRequest)
  })
_sym_db.RegisterMessage(DetailedScanRequest)

UseOneTimeTokenRequest = _reflection.GeneratedProtocolMessageType('UseOneTimeTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _USEONETIMETOKENREQUEST,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.UseOneTimeTokenRequest)
  })
_sym_db.RegisterMessage(UseOneTimeTokenRequest)

BreachEvent = _reflection.GeneratedProtocolMessageType('BreachEvent', (_message.Message,), {
  'DESCRIPTOR' : _BREACHEVENT,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.BreachEvent)
  })
_sym_db.RegisterMessage(BreachEvent)

UseOneTimeTokenResponse = _reflection.GeneratedProtocolMessageType('UseOneTimeTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _USEONETIMETOKENRESPONSE,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.UseOneTimeTokenResponse)
  })
_sym_db.RegisterMessage(UseOneTimeTokenResponse)

OneTimeUseToken = _reflection.GeneratedProtocolMessageType('OneTimeUseToken', (_message.Message,), {
  'DESCRIPTOR' : _ONETIMEUSETOKEN,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.OneTimeUseToken)
  })
_sym_db.RegisterMessage(OneTimeUseToken)

FreePasswordScanRequest = _reflection.GeneratedProtocolMessageType('FreePasswordScanRequest', (_message.Message,), {
  'DESCRIPTOR' : _FREEPASSWORDSCANREQUEST,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.FreePasswordScanRequest)
  })
_sym_db.RegisterMessage(FreePasswordScanRequest)

FreePasswordScanResponse = _reflection.GeneratedProtocolMessageType('FreePasswordScanResponse', (_message.Message,), {
  'DESCRIPTOR' : _FREEPASSWORDSCANRESPONSE,
  '__module__' : 'breachwatch_pb2'
  # @@protoc_insertion_point(class_scope:BreachWatch.FreePasswordScanResponse)
  })
_sym_db.RegisterMessage(FreePasswordScanResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.keepersecurity.protoB\013BreachWatch'
  _BREACHWATCHINFOTYPE._serialized_start=1772
  _BREACHWATCHINFOTYPE._serialized_end=1829
  _BREACHWATCHRECORDREQUEST._serialized_start=35
  _BREACHWATCHRECORDREQUEST._serialized_end=196
  _BREACHWATCHUPDATEREQUEST._serialized_start=198
  _BREACHWATCHUPDATEREQUEST._serialized_end=320
  _BREACHWATCHRECORDSTATUS._serialized_start=322
  _BREACHWATCHRECORDSTATUS._serialized_end=398
  _BREACHWATCHUPDATERESPONSE._serialized_start=400
  _BREACHWATCHUPDATERESPONSE._serialized_end=498
  _BREACHWATCHTOKENREQUEST._serialized_start=500
  _BREACHWATCHTOKENREQUEST._serialized_end=551
  _BREACHWATCHTOKENRESPONSE._serialized_start=553
  _BREACHWATCHTOKENRESPONSE._serialized_end=630
  _ANONYMIZEDTOKENRESPONSE._serialized_start=632
  _ANONYMIZEDTOKENRESPONSE._serialized_end=721
  _HASHCHECK._serialized_start=723
  _HASHCHECK._serialized_end=763
  _BREACHWATCHSTATUSREQUEST._serialized_start=765
  _BREACHWATCHSTATUSREQUEST._serialized_end=880
  _HASHSTATUS._serialized_start=882
  _HASHSTATUS._serialized_end=947
  _BREACHWATCHSTATUSRESPONSE._serialized_start=949
  _BREACHWATCHSTATUSRESPONSE._serialized_end=1021
  _ENTERPRISEPUBLICKEYRESPONSE._serialized_start=1023
  _ENTERPRISEPUBLICKEYRESPONSE._serialized_end=1113
  _FREESCANREQUEST._serialized_start=1115
  _FREESCANREQUEST._serialized_end=1153
  _FREESCANRESPONSE._serialized_start=1155
  _FREESCANRESPONSE._serialized_end=1222
  _PAIDUSERREQUEST._serialized_start=1224
  _PAIDUSERREQUEST._serialized_end=1256
  _PAIDUSERRESPONSE._serialized_start=1258
  _PAIDUSERRESPONSE._serialized_end=1294
  _DETAILEDSCANREQUEST._serialized_start=1296
  _DETAILEDSCANREQUEST._serialized_end=1332
  _USEONETIMETOKENREQUEST._serialized_start=1334
  _USEONETIMETOKENREQUEST._serialized_end=1373
  _BREACHEVENT._serialized_start=1375
  _BREACHEVENT._serialized_end=1478
  _USEONETIMETOKENRESPONSE._serialized_start=1481
  _USEONETIMETOKENRESPONSE._serialized_end=1618
  _ONETIMEUSETOKEN._serialized_start=1620
  _ONETIMEUSETOKEN._serialized_end=1665
  _FREEPASSWORDSCANREQUEST._serialized_start=1667
  _FREEPASSWORDSCANREQUEST._serialized_end=1716
  _FREEPASSWORDSCANRESPONSE._serialized_start=1718
  _FREEPASSWORDSCANRESPONSE._serialized_end=1770
# @@protoc_insertion_point(module_scope)
