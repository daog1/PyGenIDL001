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
class UpdateAmmsArgs(typing.TypedDict):
    marketIndexes:list[int]


layout = borsh.CStruct(
    "marketIndexes" /borsh.U16[5],
    )


class UpdateAmmsAccounts(typing.TypedDict):
    state:SolPubkey
    authority:SolPubkey

def UpdateAmms(
    args: UpdateAmmsArgs,
    accounts: UpdateAmmsAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["state"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["authority"], is_signer=True, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xc9\x6a\xd9\xfd\x04\xaf\xe4\x61"
    encoded_args = layout.build({
        "marketIndexes":args["marketIndexes"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)




