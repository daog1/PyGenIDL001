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

class DepositPausedJSON(typing.TypedDict):
    kind: typing.Literal["DepositPaused"]


@dataclass
class DepositPaused:
    discriminator: typing.ClassVar = 0
    @classmethod
    def to_json(cls) -> DepositPausedJSON:
        return DepositPausedJSON(
            kind="DepositPaused",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "DepositPaused": {},
        }



class WithdrawPausedJSON(typing.TypedDict):
    kind: typing.Literal["WithdrawPaused"]


@dataclass
class WithdrawPaused:
    discriminator: typing.ClassVar = 1
    @classmethod
    def to_json(cls) -> WithdrawPausedJSON:
        return WithdrawPausedJSON(
            kind="WithdrawPaused",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "WithdrawPaused": {},
        }



class AmmPausedJSON(typing.TypedDict):
    kind: typing.Literal["AmmPaused"]


@dataclass
class AmmPaused:
    discriminator: typing.ClassVar = 2
    @classmethod
    def to_json(cls) -> AmmPausedJSON:
        return AmmPausedJSON(
            kind="AmmPaused",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "AmmPaused": {},
        }



class FillPausedJSON(typing.TypedDict):
    kind: typing.Literal["FillPaused"]


@dataclass
class FillPaused:
    discriminator: typing.ClassVar = 3
    @classmethod
    def to_json(cls) -> FillPausedJSON:
        return FillPausedJSON(
            kind="FillPaused",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "FillPaused": {},
        }



class LiqPausedJSON(typing.TypedDict):
    kind: typing.Literal["LiqPaused"]


@dataclass
class LiqPaused:
    discriminator: typing.ClassVar = 4
    @classmethod
    def to_json(cls) -> LiqPausedJSON:
        return LiqPausedJSON(
            kind="LiqPaused",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "LiqPaused": {},
        }



class FundingPausedJSON(typing.TypedDict):
    kind: typing.Literal["FundingPaused"]


@dataclass
class FundingPaused:
    discriminator: typing.ClassVar = 5
    @classmethod
    def to_json(cls) -> FundingPausedJSON:
        return FundingPausedJSON(
            kind="FundingPaused",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "FundingPaused": {},
        }



class SettlePnlPausedJSON(typing.TypedDict):
    kind: typing.Literal["SettlePnlPaused"]


@dataclass
class SettlePnlPaused:
    discriminator: typing.ClassVar = 6
    @classmethod
    def to_json(cls) -> SettlePnlPausedJSON:
        return SettlePnlPausedJSON(
            kind="SettlePnlPaused",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "SettlePnlPaused": {},
        }



class AmmImmediateFillPausedJSON(typing.TypedDict):
    kind: typing.Literal["AmmImmediateFillPaused"]


@dataclass
class AmmImmediateFillPaused:
    discriminator: typing.ClassVar = 7
    @classmethod
    def to_json(cls) -> AmmImmediateFillPausedJSON:
        return AmmImmediateFillPausedJSON(
            kind="AmmImmediateFillPaused",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "AmmImmediateFillPaused": {},
        }





ExchangeStatusKind = typing.Union[
DepositPaused,
WithdrawPaused,
AmmPaused,
FillPaused,
LiqPaused,
FundingPaused,
SettlePnlPaused,
AmmImmediateFillPaused,
]
ExchangeStatusJSON = typing.Union[
DepositPausedJSON,
WithdrawPausedJSON,
AmmPausedJSON,
FillPausedJSON,
LiqPausedJSON,
FundingPausedJSON,
SettlePnlPausedJSON,
AmmImmediateFillPausedJSON,
]

def from_decoded(obj: dict) -> ExchangeStatusKind:
    if not isinstance(obj, dict):
        raise ValueError("Invalid enum object")
    if "DepositPaused" in obj:
      return DepositPaused()
    if "WithdrawPaused" in obj:
      return WithdrawPaused()
    if "AmmPaused" in obj:
      return AmmPaused()
    if "FillPaused" in obj:
      return FillPaused()
    if "LiqPaused" in obj:
      return LiqPaused()
    if "FundingPaused" in obj:
      return FundingPaused()
    if "SettlePnlPaused" in obj:
      return SettlePnlPaused()
    if "AmmImmediateFillPaused" in obj:
      return AmmImmediateFillPaused()
    raise ValueError("Invalid enum object")

def from_json(obj: ExchangeStatusJSON) -> ExchangeStatusKind:
    if obj["kind"] == "DepositPaused":
        return DepositPaused()
    if obj["kind"] == "WithdrawPaused":
        return WithdrawPaused()
    if obj["kind"] == "AmmPaused":
        return AmmPaused()
    if obj["kind"] == "FillPaused":
        return FillPaused()
    if obj["kind"] == "LiqPaused":
        return LiqPaused()
    if obj["kind"] == "FundingPaused":
        return FundingPaused()
    if obj["kind"] == "SettlePnlPaused":
        return SettlePnlPaused()
    if obj["kind"] == "AmmImmediateFillPaused":
        return AmmImmediateFillPaused()
    kind = obj["kind"]
    raise ValueError(f"Unrecognized enum kind: {kind}")

layout = EnumForCodegen(
"DepositPaused" / borsh.CStruct(),
"WithdrawPaused" / borsh.CStruct(),
"AmmPaused" / borsh.CStruct(),
"FillPaused" / borsh.CStruct(),
"LiqPaused" / borsh.CStruct(),
"FundingPaused" / borsh.CStruct(),
"SettlePnlPaused" / borsh.CStruct(),
"AmmImmediateFillPaused" / borsh.CStruct(),
)
