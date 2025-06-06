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
class DeleteInitializedPerpMarketArgs(typing.TypedDict):
    marketIndex:int


layout = borsh.CStruct(
    "marketIndex" /borsh.U16,
    )


class DeleteInitializedPerpMarketAccounts(typing.TypedDict):
    admin:SolPubkey
    state:SolPubkey
    perpMarket:SolPubkey

def DeleteInitializedPerpMarket(
    args: DeleteInitializedPerpMarketArgs,
    accounts: DeleteInitializedPerpMarketAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["admin"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["state"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["perpMarket"], is_signer=False, is_writable=True),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x5b\x9a\x18\x57\x6a\x3b\xbe\x42"
    encoded_args = layout.build({
        "marketIndex":args["marketIndex"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



