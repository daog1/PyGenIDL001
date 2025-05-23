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

class StandardJSON(typing.TypedDict):
    kind: typing.Literal["Standard"]


@dataclass
class Standard:
    discriminator: typing.ClassVar = 0
    @classmethod
    def to_json(cls) -> StandardJSON:
        return StandardJSON(
            kind="Standard",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "Standard": {},
        }



class ConstantProductJSON(typing.TypedDict):
    kind: typing.Literal["ConstantProduct"]


@dataclass
class ConstantProduct:
    discriminator: typing.ClassVar = 1
    @classmethod
    def to_json(cls) -> ConstantProductJSON:
        return ConstantProductJSON(
            kind="ConstantProduct",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "ConstantProduct": {},
        }





CurveTypeKind = typing.Union[
Standard,
ConstantProduct,
]
CurveTypeJSON = typing.Union[
StandardJSON,
ConstantProductJSON,
]

def from_decoded(obj: dict) -> CurveTypeKind:
    if not isinstance(obj, dict):
        raise ValueError("Invalid enum object")
    if "Standard" in obj:
      return Standard()
    if "ConstantProduct" in obj:
      return ConstantProduct()
    raise ValueError("Invalid enum object")

def from_json(obj: CurveTypeJSON) -> CurveTypeKind:
    if obj["kind"] == "Standard":
        return Standard()
    if obj["kind"] == "ConstantProduct":
        return ConstantProduct()
    kind = obj["kind"]
    raise ValueError(f"Unrecognized enum kind: {kind}")

layout = EnumForCodegen(
"Standard" / borsh.CStruct(),
"ConstantProduct" / borsh.CStruct(),
)
