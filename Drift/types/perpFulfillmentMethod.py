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

class AMMJSON(typing.TypedDict):
    kind: typing.Literal["AMM"]


@dataclass
class AMM:
    discriminator: typing.ClassVar = 0
    @classmethod
    def to_json(cls) -> AMMJSON:
        return AMMJSON(
            kind="AMM",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "AMM": {},
        }



class MatchJSON(typing.TypedDict):
    kind: typing.Literal["Match"]


@dataclass
class Match:
    discriminator: typing.ClassVar = 1
    @classmethod
    def to_json(cls) -> MatchJSON:
        return MatchJSON(
            kind="Match",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "Match": {},
        }





PerpFulfillmentMethodKind = typing.Union[
AMM,
Match,
]
PerpFulfillmentMethodJSON = typing.Union[
AMMJSON,
MatchJSON,
]

def from_decoded(obj: dict) -> PerpFulfillmentMethodKind:
    if not isinstance(obj, dict):
        raise ValueError("Invalid enum object")
    if "AMM" in obj:
      return AMM()
    if "Match" in obj:
      return Match()
    raise ValueError("Invalid enum object")

def from_json(obj: PerpFulfillmentMethodJSON) -> PerpFulfillmentMethodKind:
    if obj["kind"] == "AMM":
        return AMM()
    if obj["kind"] == "Match":
        return Match()
    kind = obj["kind"]
    raise ValueError(f"Unrecognized enum kind: {kind}")

layout = EnumForCodegen(
"AMM" / borsh.CStruct(),
"Match" / borsh.CStruct(),
)
