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
from . import marketType

class MarketIdentifierJSON(typing.TypedDict):
    marketType: marketType.MarketTypeJSON
    marketIndex: int

@dataclass
class MarketIdentifier:
    layout: typing.ClassVar = borsh.CStruct(
        "marketType" /marketType.layout,
        "marketIndex" /borsh.U16,
        )
    #fields
    marketType: marketType.MarketTypeKind
    marketIndex: int
    
    @classmethod
    def from_decoded(cls, obj: Container) -> "MarketIdentifier":
        return cls(
        marketType=marketType.from_decoded(obj["marketType"]),
        marketIndex=obj["marketIndex"],
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
                "marketType": self.marketType.to_encodable(),
                "marketIndex": self.marketIndex,
                }

    def to_json(self) -> MarketIdentifierJSON:
        return {
                "marketType": self.marketType.to_json(),
                "marketIndex": self.marketIndex,
                }

    @classmethod
    def from_json(cls, obj: MarketIdentifierJSON) -> "MarketIdentifier":
        return cls(
                marketType=marketType.from_json(obj["marketType"]),
                marketIndex=obj["marketIndex"],
        )






