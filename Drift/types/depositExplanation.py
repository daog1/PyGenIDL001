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


class NoneJSON(typing.TypedDict):
    kind: typing.Literal["None"]


@dataclass
class None_:
    discriminator: typing.ClassVar = 0
    def to_json(self) -> NoneJSON:
        return NoneJSON(
            kind="None",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "None": {},
        }




class TransferJSON(typing.TypedDict):
    kind: typing.Literal["Transfer"]


@dataclass
class Transfer:
    discriminator: typing.ClassVar = 1
    def to_json(self) -> TransferJSON:
        return TransferJSON(
            kind="Transfer",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "Transfer": {},
        }




class BorrowJSON(typing.TypedDict):
    kind: typing.Literal["Borrow"]


@dataclass
class Borrow:
    discriminator: typing.ClassVar = 2
    def to_json(self) -> BorrowJSON:
        return BorrowJSON(
            kind="Borrow",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "Borrow": {},
        }




class RepayBorrowJSON(typing.TypedDict):
    kind: typing.Literal["RepayBorrow"]


@dataclass
class RepayBorrow:
    discriminator: typing.ClassVar = 3
    def to_json(self) -> RepayBorrowJSON:
        return RepayBorrowJSON(
            kind="RepayBorrow",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "RepayBorrow": {},
        }





DepositExplanationKind = typing.Union[
    None_,
    Transfer,
    Borrow,
    RepayBorrow,
]
DepositExplanationJSON = typing.Union[
    NoneJSON,
    TransferJSON,
    BorrowJSON,
    RepayBorrowJSON,
]

def from_decoded(obj: dict) -> DepositExplanationKind:
    if not isinstance(obj, dict):
        raise ValueError("Invalid enum object")
    if "None" in obj:
      return None_()
    if "Transfer" in obj:
      return Transfer()
    if "Borrow" in obj:
      return Borrow()
    if "RepayBorrow" in obj:
      return RepayBorrow()
    raise ValueError("Invalid enum object")

def from_json(obj: DepositExplanationJSON) -> DepositExplanationKind:
    if obj["kind"] == "None":
        return None_()

    if obj["kind"] == "Transfer":
        return Transfer()

    if obj["kind"] == "Borrow":
        return Borrow()

    if obj["kind"] == "RepayBorrow":
        return RepayBorrow()

    kind = obj["kind"]
    raise ValueError(f"Unrecognized enum kind: {kind}")


layout = EnumForCodegen(
"None" / borsh.CStruct(),
"Transfer" / borsh.CStruct(),
"Borrow" / borsh.CStruct(),
"RepayBorrow" / borsh.CStruct(),
)
