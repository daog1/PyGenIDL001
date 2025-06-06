'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from construct import Construct
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import PROGRAM_ID
class RefreshPythLazerPriceArgs(typing.TypedDict):
    tokens:list[int]
    serializedPythMessage:str
    ed25519InstructionIndex:int


layout = borsh.CStruct(
    "tokens" /borsh.Vec(typing.cast(Construct, borsh.U16)),
    "serializedPythMessage" /borsh.String,
    "ed25519InstructionIndex" /borsh.U16,
    )


class RefreshPythLazerPriceAccounts(typing.TypedDict):
    user:SolPubkey
    oraclePrices:SolPubkey
    oracleMappings:SolPubkey
    oracleTwaps:SolPubkey
    pythProgram:SolPubkey
    pythStorage:SolPubkey
    pythTreasury:SolPubkey
    systemProgram:SolPubkey
    instructionsSysvar:SolPubkey

def RefreshPythLazerPrice(
    args: RefreshPythLazerPriceArgs,
    accounts: RefreshPythLazerPriceAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["user"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["oraclePrices"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["oracleMappings"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["oracleTwaps"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["pythProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["pythStorage"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["pythTreasury"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["systemProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["instructionsSysvar"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x7a\x2f\xb1\x85\xb1\x23\x5d\x76"
    encoded_args = layout.build({
        "tokens":args["tokens"],
        "serializedPythMessage":args["serializedPythMessage"],
        "ed25519InstructionIndex":args["ed25519InstructionIndex"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)






