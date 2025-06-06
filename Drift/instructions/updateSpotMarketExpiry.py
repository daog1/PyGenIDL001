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
class UpdateSpotMarketExpiryArgs(typing.TypedDict):
    expiryTs:int


layout = borsh.CStruct(
    "expiryTs" /borsh.I64,
    )


class UpdateSpotMarketExpiryAccounts(typing.TypedDict):
    admin:SolPubkey
    state:SolPubkey
    spotMarket:SolPubkey

def UpdateSpotMarketExpiry(
    args: UpdateSpotMarketExpiryArgs,
    accounts: UpdateSpotMarketExpiryAccounts,
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
    identifier = b"\xd0\x0b\xd3\x9f\xe2\x18\x0b\xf7"
    encoded_args = layout.build({
        "expiryTs":args["expiryTs"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



