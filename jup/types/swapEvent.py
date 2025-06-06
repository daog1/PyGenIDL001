'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from anchorpy.borsh_extension import BorshPubkey
from construct import Container
from dataclasses import dataclass
from solders.pubkey import Pubkey as SolPubkey

class SwapEventJSON(typing.TypedDict):
    amm: str
    inputMint: str
    inputAmount: int
    outputMint: str
    outputAmount: int

@dataclass
class SwapEvent:
    layout: typing.ClassVar = borsh.CStruct(
        "amm" /BorshPubkey,
        "inputMint" /BorshPubkey,
        "inputAmount" /borsh.U64,
        "outputMint" /BorshPubkey,
        "outputAmount" /borsh.U64,
        )
    #fields
    amm: SolPubkey
    inputMint: SolPubkey
    inputAmount: int
    outputMint: SolPubkey
    outputAmount: int
    
    @classmethod
    def from_decoded(cls, obj: Container) -> "SwapEvent":
        return cls(
        amm=obj["amm"],
        inputMint=obj["inputMint"],
        inputAmount=obj["inputAmount"],
        outputMint=obj["outputMint"],
        outputAmount=obj["outputAmount"],
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
                "amm": self.amm,
                "inputMint": self.inputMint,
                "inputAmount": self.inputAmount,
                "outputMint": self.outputMint,
                "outputAmount": self.outputAmount,
                }

    def to_json(self) -> SwapEventJSON:
        return {
                "amm": str(self.amm),
                "inputMint": str(self.inputMint),
                "inputAmount": self.inputAmount,
                "outputMint": str(self.outputMint),
                "outputAmount": self.outputAmount,
                }

    @classmethod
    def from_json(cls, obj: SwapEventJSON) -> "SwapEvent":
        return cls(
                amm=SolPubkey.from_string(obj["amm"]),
                inputMint=SolPubkey.from_string(obj["inputMint"]),
                inputAmount=obj["inputAmount"],
                outputMint=SolPubkey.from_string(obj["outputMint"]),
                outputAmount=obj["outputAmount"],
        )






