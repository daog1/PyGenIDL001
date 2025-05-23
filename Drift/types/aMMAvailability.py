'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh;
import typing;
from anchorpy.borsh_extension import BorshPubkey, EnumForCodegen;
from construct import Container;
from dataclasses import dataclass;
from solders.pubkey import Pubkey;
from solders.sysvar import RENT;

class ImmediateJSON(typing.TypedDict):
    kind: typing.Literal["Immediate"]


@dataclass
class Immediate:
    discriminator: typing.ClassVar = 0
    @classmethod
    def to_json(cls) -> ImmediateJSON:
        return ImmediateJSON(
            kind="Immediate",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "Immediate": {},
        }



class AfterMinDurationJSON(typing.TypedDict):
    kind: typing.Literal["AfterMinDuration"]


@dataclass
class AfterMinDuration:
    discriminator: typing.ClassVar = 1
    @classmethod
    def to_json(cls) -> AfterMinDurationJSON:
        return AfterMinDurationJSON(
            kind="AfterMinDuration",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "AfterMinDuration": {},
        }



class UnavailableJSON(typing.TypedDict):
    kind: typing.Literal["Unavailable"]


@dataclass
class Unavailable:
    discriminator: typing.ClassVar = 2
    @classmethod
    def to_json(cls) -> UnavailableJSON:
        return UnavailableJSON(
            kind="Unavailable",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "Unavailable": {},
        }





AMMAvailabilityKind = typing.Union[
Immediate,
AfterMinDuration,
Unavailable,
]
AMMAvailabilityJSON = typing.Union[
ImmediateJSON,
AfterMinDurationJSON,
UnavailableJSON,
]

def from_decoded(obj: dict) -> AMMAvailabilityKind:
    if not isinstance(obj, dict):
        raise ValueError("Invalid enum object")
    if "Immediate" in obj:
      return Immediate()
    if "AfterMinDuration" in obj:
      return AfterMinDuration()
    if "Unavailable" in obj:
      return Unavailable()
    raise ValueError("Invalid enum object")

def from_json(obj: AMMAvailabilityJSON) -> AMMAvailabilityKind:
    if obj["kind"] == "Immediate":
        return Immediate()
    if obj["kind"] == "AfterMinDuration":
        return AfterMinDuration()
    if obj["kind"] == "Unavailable":
        return Unavailable()
    kind = obj["kind"]
    raise ValueError(f"Unrecognized enum kind: {kind}")

layout = EnumForCodegen(
"Immediate" / borsh.CStruct(),
"AfterMinDuration" / borsh.CStruct(),
"Unavailable" / borsh.CStruct(),
)
