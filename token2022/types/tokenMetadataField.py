'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from anchorpy.borsh_extension import EnumForCodegen
from dataclasses import dataclass


class NameJSON(typing.TypedDict):
    kind: typing.Literal["Name"]


@dataclass
class Name:
    discriminator: typing.ClassVar = 0
    def to_json(self) -> NameJSON:
        return NameJSON(
            kind="Name",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "Name": {},
        }




class SymbolJSON(typing.TypedDict):
    kind: typing.Literal["Symbol"]


@dataclass
class Symbol:
    discriminator: typing.ClassVar = 1
    def to_json(self) -> SymbolJSON:
        return SymbolJSON(
            kind="Symbol",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "Symbol": {},
        }




class UriJSON(typing.TypedDict):
    kind: typing.Literal["Uri"]


@dataclass
class Uri:
    discriminator: typing.ClassVar = 2
    def to_json(self) -> UriJSON:
        return UriJSON(
            kind="Uri",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "Uri": {},
        }



KeyJSONValue = tuple[str]
KeyValue = tuple[str]

class KeyJSON(typing.TypedDict):
    kind: typing.Literal["Key"]
    value: KeyJSONValue


@dataclass
class Key:
    discriminator: typing.ClassVar = 3
    value : KeyValue
    def to_json(self) -> KeyJSON:
        return KeyJSON(
            kind="Key",
            value = (self.value[0],)
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "Key": { "item_0":self.value[0] }
        }





TokenMetadataFieldKind = typing.Union[
    Name,
    Symbol,
    Uri,
    Key,
]
TokenMetadataFieldJSON = typing.Union[
    NameJSON,
    SymbolJSON,
    UriJSON,
    KeyJSON,
]

def from_decoded(obj: dict) -> TokenMetadataFieldKind:
    if not isinstance(obj, dict):
        raise ValueError("Invalid enum object")
    if "Name" in obj:
      return Name()
    if "Symbol" in obj:
      return Symbol()
    if "Uri" in obj:
      return Uri()
    if "Key" in obj:
      val = obj["Key"]
      return Key((
      val["item_0"],
      ))
    raise ValueError("Invalid enum object")

def from_json(obj: TokenMetadataFieldJSON) -> TokenMetadataFieldKind:
    if obj["kind"] == "Name":
        return Name()

    if obj["kind"] == "Symbol":
        return Symbol()

    if obj["kind"] == "Uri":
        return Uri()

    if obj["kind"] == "Key":
        keyJSONValue = typing.cast(KeyJSONValue, obj["value"])
        return Key(
        (keyJSONValue[0],)
        )

    kind = obj["kind"]
    raise ValueError(f"Unrecognized enum kind: {kind}")


layout = EnumForCodegen(
"Name" / borsh.CStruct(),
"Symbol" / borsh.CStruct(),
"Uri" / borsh.CStruct(),
"Key" / borsh.CStruct("item_0" / borsh.String,),
)
