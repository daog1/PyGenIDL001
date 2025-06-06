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

class HistoricalIndexDataJSON(typing.TypedDict):
    lastIndexBidPrice: int
    lastIndexAskPrice: int
    lastIndexPriceTwap: int
    lastIndexPriceTwap5min: int
    lastIndexPriceTwapTs: int

@dataclass
class HistoricalIndexData:
    layout: typing.ClassVar = borsh.CStruct(
        "lastIndexBidPrice" /borsh.U64,
        "lastIndexAskPrice" /borsh.U64,
        "lastIndexPriceTwap" /borsh.U64,
        "lastIndexPriceTwap5min" /borsh.U64,
        "lastIndexPriceTwapTs" /borsh.I64,
        )
    #fields
    lastIndexBidPrice: int
    lastIndexAskPrice: int
    lastIndexPriceTwap: int
    lastIndexPriceTwap5min: int
    lastIndexPriceTwapTs: int
    
    @classmethod
    def from_decoded(cls, obj: Container) -> "HistoricalIndexData":
        return cls(
        lastIndexBidPrice=obj["lastIndexBidPrice"],
        lastIndexAskPrice=obj["lastIndexAskPrice"],
        lastIndexPriceTwap=obj["lastIndexPriceTwap"],
        lastIndexPriceTwap5min=obj["lastIndexPriceTwap5min"],
        lastIndexPriceTwapTs=obj["lastIndexPriceTwapTs"],
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
                "lastIndexBidPrice": self.lastIndexBidPrice,
                "lastIndexAskPrice": self.lastIndexAskPrice,
                "lastIndexPriceTwap": self.lastIndexPriceTwap,
                "lastIndexPriceTwap5min": self.lastIndexPriceTwap5min,
                "lastIndexPriceTwapTs": self.lastIndexPriceTwapTs,
                }

    def to_json(self) -> HistoricalIndexDataJSON:
        return {
                "lastIndexBidPrice": self.lastIndexBidPrice,
                "lastIndexAskPrice": self.lastIndexAskPrice,
                "lastIndexPriceTwap": self.lastIndexPriceTwap,
                "lastIndexPriceTwap5min": self.lastIndexPriceTwap5min,
                "lastIndexPriceTwapTs": self.lastIndexPriceTwapTs,
                }

    @classmethod
    def from_json(cls, obj: HistoricalIndexDataJSON) -> "HistoricalIndexData":
        return cls(
                lastIndexBidPrice=obj["lastIndexBidPrice"],
                lastIndexAskPrice=obj["lastIndexAskPrice"],
                lastIndexPriceTwap=obj["lastIndexPriceTwap"],
                lastIndexPriceTwap5min=obj["lastIndexPriceTwap5min"],
                lastIndexPriceTwapTs=obj["lastIndexPriceTwapTs"],
        )






