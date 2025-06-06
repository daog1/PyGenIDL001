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

class SpotBankruptcyRecordJSON(typing.TypedDict):
    marketIndex: int
    borrowAmount: int
    ifPayment: int
    cumulativeDepositInterestDelta: int

@dataclass
class SpotBankruptcyRecord:
    layout: typing.ClassVar = borsh.CStruct(
        "marketIndex" /borsh.U16,
        "borrowAmount" /borsh.U128,
        "ifPayment" /borsh.U128,
        "cumulativeDepositInterestDelta" /borsh.U128,
        )
    #fields
    marketIndex: int
    borrowAmount: int
    ifPayment: int
    cumulativeDepositInterestDelta: int
    
    @classmethod
    def from_decoded(cls, obj: Container) -> "SpotBankruptcyRecord":
        return cls(
        marketIndex=obj["marketIndex"],
        borrowAmount=obj["borrowAmount"],
        ifPayment=obj["ifPayment"],
        cumulativeDepositInterestDelta=obj["cumulativeDepositInterestDelta"],
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
                "marketIndex": self.marketIndex,
                "borrowAmount": self.borrowAmount,
                "ifPayment": self.ifPayment,
                "cumulativeDepositInterestDelta": self.cumulativeDepositInterestDelta,
                }

    def to_json(self) -> SpotBankruptcyRecordJSON:
        return {
                "marketIndex": self.marketIndex,
                "borrowAmount": self.borrowAmount,
                "ifPayment": self.ifPayment,
                "cumulativeDepositInterestDelta": self.cumulativeDepositInterestDelta,
                }

    @classmethod
    def from_json(cls, obj: SpotBankruptcyRecordJSON) -> "SpotBankruptcyRecord":
        return cls(
                marketIndex=obj["marketIndex"],
                borrowAmount=obj["borrowAmount"],
                ifPayment=obj["ifPayment"],
                cumulativeDepositInterestDelta=obj["cumulativeDepositInterestDelta"],
        )






