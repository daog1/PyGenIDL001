'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from construct import GreedyBytes
from dataclasses import dataclass
from ..shared import FixedSizeBytes

EncryptedBalance=FixedSizeBytes(64,GreedyBytes)
pyType = bytes

