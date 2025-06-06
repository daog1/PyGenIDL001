'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from anchorpy.borsh_extension import BorshPubkey
from construct import Container
from dataclasses import dataclass
from solders.pubkey import Pubkey as SolPubkey

class UpdateGlobalAuthorityEventJSON(typing.TypedDict):
    global_: str
    authority: str
    newAuthority: str
    timestamp: int

@dataclass
class UpdateGlobalAuthorityEvent:
    layout: typing.ClassVar = borsh.CStruct(
        "global" /BorshPubkey,
        "authority" /BorshPubkey,
        "newAuthority" /BorshPubkey,
        "timestamp" /borsh.I64,
        )
    #fields
    global_: SolPubkey
    authority: SolPubkey
    newAuthority: SolPubkey
    timestamp: int
    
    @classmethod
    def from_decoded(cls, obj: Container) -> "UpdateGlobalAuthorityEvent":
        return cls(
        global_=obj["global"],
        authority=obj["authority"],
        newAuthority=obj["newAuthority"],
        timestamp=obj["timestamp"],
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
                "global": self.global_,
                "authority": self.authority,
                "newAuthority": self.newAuthority,
                "timestamp": self.timestamp,
                }

    def to_json(self) -> UpdateGlobalAuthorityEventJSON:
        return {
                "global_": str(self.global_),
                "authority": str(self.authority),
                "newAuthority": str(self.newAuthority),
                "timestamp": self.timestamp,
                }

    @classmethod
    def from_json(cls, obj: UpdateGlobalAuthorityEventJSON) -> "UpdateGlobalAuthorityEvent":
        return cls(
                global_=SolPubkey.from_string(obj["global_"]),
                authority=SolPubkey.from_string(obj["authority"]),
                newAuthority=SolPubkey.from_string(obj["newAuthority"]),
                timestamp=obj["timestamp"],
        )






