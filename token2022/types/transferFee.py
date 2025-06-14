'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from construct import Container
from dataclasses import dataclass

class TransferFeeJSON(typing.TypedDict):
    epoch: int
    maximumFee: int
    transferFeeBasisPoints: int

@dataclass
class TransferFee:
    layout: typing.ClassVar = borsh.CStruct(
        "epoch" /borsh.U64,
        "maximumFee" /borsh.U64,
        "transferFeeBasisPoints" /borsh.U16,
        )
    #fields
    epoch: int
    maximumFee: int
    transferFeeBasisPoints: int
    
    @classmethod
    def from_decoded(cls, obj: Container) -> "TransferFee":
        return cls(
        epoch=obj["epoch"],
        maximumFee=obj["maximumFee"],
        transferFeeBasisPoints=obj["transferFeeBasisPoints"],
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
                "epoch": self.epoch,
                "maximumFee": self.maximumFee,
                "transferFeeBasisPoints": self.transferFeeBasisPoints,
                }

    def to_json(self) -> TransferFeeJSON:
        return {
                "epoch": self.epoch,
                "maximumFee": self.maximumFee,
                "transferFeeBasisPoints": self.transferFeeBasisPoints,
                }

    @classmethod
    def from_json(cls, obj: TransferFeeJSON) -> "TransferFee":
        return cls(
                epoch=obj["epoch"],
                maximumFee=obj["maximumFee"],
                transferFeeBasisPoints=obj["transferFeeBasisPoints"],
        )






