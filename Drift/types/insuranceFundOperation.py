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


class InitJSON(typing.TypedDict):
    kind: typing.Literal["Init"]


@dataclass
class Init:
    discriminator: typing.ClassVar = 0
    def to_json(self) -> InitJSON:
        return InitJSON(
            kind="Init",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "Init": {},
        }




class AddJSON(typing.TypedDict):
    kind: typing.Literal["Add"]


@dataclass
class Add:
    discriminator: typing.ClassVar = 1
    def to_json(self) -> AddJSON:
        return AddJSON(
            kind="Add",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "Add": {},
        }




class RequestRemoveJSON(typing.TypedDict):
    kind: typing.Literal["RequestRemove"]


@dataclass
class RequestRemove:
    discriminator: typing.ClassVar = 2
    def to_json(self) -> RequestRemoveJSON:
        return RequestRemoveJSON(
            kind="RequestRemove",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "RequestRemove": {},
        }




class RemoveJSON(typing.TypedDict):
    kind: typing.Literal["Remove"]


@dataclass
class Remove:
    discriminator: typing.ClassVar = 3
    def to_json(self) -> RemoveJSON:
        return RemoveJSON(
            kind="Remove",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "Remove": {},
        }





InsuranceFundOperationKind = typing.Union[
    Init,
    Add,
    RequestRemove,
    Remove,
]
InsuranceFundOperationJSON = typing.Union[
    InitJSON,
    AddJSON,
    RequestRemoveJSON,
    RemoveJSON,
]

def from_decoded(obj: dict) -> InsuranceFundOperationKind:
    if not isinstance(obj, dict):
        raise ValueError("Invalid enum object")
    if "Init" in obj:
      return Init()
    if "Add" in obj:
      return Add()
    if "RequestRemove" in obj:
      return RequestRemove()
    if "Remove" in obj:
      return Remove()
    raise ValueError("Invalid enum object")

def from_json(obj: InsuranceFundOperationJSON) -> InsuranceFundOperationKind:
    if obj["kind"] == "Init":
        return Init()

    if obj["kind"] == "Add":
        return Add()

    if obj["kind"] == "RequestRemove":
        return RequestRemove()

    if obj["kind"] == "Remove":
        return Remove()

    kind = obj["kind"]
    raise ValueError(f"Unrecognized enum kind: {kind}")


layout = EnumForCodegen(
"Init" / borsh.CStruct(),
"Add" / borsh.CStruct(),
"RequestRemove" / borsh.CStruct(),
"Remove" / borsh.CStruct(),
)
