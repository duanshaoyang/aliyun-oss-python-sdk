# -*- coding: utf-8 -*-
"""
oss2.headers
~~~~~~~~
这个模块包含http请求里header的key定义
同时包含了发送http请求的header, 类型为dict
"""
OSS_USER_METADATA_PREFIX = "x-oss-meta-";

OSS_CANNED_ACL = "x-oss-acl";

OSS_OBJECT_IF_UNMODIFIED_SINCE = "If-Unmodified-Since";
OSS_OBJECT_IF_MATCH = "If-Match";

COPY_OBJECT_SOURCE = "x-oss-copy-source";
COPY_SOURCE_RANGE = "x-oss-copy-source-range";

OSS_HEADER_REQUEST_ID = "x-oss-request-id";

OSS_SECURITY_TOKEN = "x-oss-security-token";

OSS_NEXT_APPEND_POSITION = "x-oss-next-append-position";
OSS_HASH_CRC64_ECMA = "x-oss-hash-crc64ecma";
OSS_OBJECT_TYPE = "x-oss-object-type";

OSS_OBJECT_ACL = "x-oss-object-acl";

OSS_HEADER_SYMLINK_TARGET = "x-oss-symlink-target";

OSS_SERVER_SIDE_ENCRYPTION = "x-oss-server-side-encryption"
OSS_SERVER_SIDE_ENCRYPTION_KEY_ID = "x-oss-server-side-encryption-key-id"

class requestHeader(dict): 
    def __init__(self, *arg, **kw): 
        super(requestHeader, self).__init__(*arg, **kw)

    def setServerSideEncryption(self, algorithm=None, cmk_id=None):
        if OSS_SERVER_SIDE_ENCRYPTION in self:
            del self[OSS_SERVER_SIDE_ENCRYPTION]
        if OSS_SERVER_SIDE_ENCRYPTION_KEY_ID in self:
            del self[OSS_SERVER_SIDE_ENCRYPTION_KEY_ID]

        if algorithm is "AES256":
            self[OSS_SERVER_SIDE_ENCRYPTION] = "AES256"
        elif algorithm is "KMS":
            self[OSS_SERVER_SIDE_ENCRYPTION] = "KMS"
            if cmk_id is not None:
                self[OSS_SERVER_SIDE_ENCRYPTION_KEY_ID] = cmk_id
