'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import PROGRAM_ID
class UpdateSpotMarketPausedOperationsArgs(typing.TypedDict):
    pausedOperations:int


layout = borsh.CStruct(
    "pausedOperations" /borsh.U8,
    )


class UpdateSpotMarketPausedOperationsAccounts(typing.TypedDict):
    admin:SolPubkey
    state:SolPubkey
    spotMarket:SolPubkey

def UpdateSpotMarketPausedOperations(
    args: UpdateSpotMarketPausedOperationsArgs,
    accounts: UpdateSpotMarketPausedOperationsAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["admin"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["state"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["spotMarket"], is_signer=False, is_writable=True),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x64\x3d\x99\x51\xb4\x0c\x06\xf8"
    encoded_args = layout.build({
        "pausedOperations":args["pausedOperations"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



