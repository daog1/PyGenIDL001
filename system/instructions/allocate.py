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
class AllocateArgs(typing.TypedDict):
    space:int


layout = borsh.CStruct(
    "space" /borsh.U64,
    )


class AllocateAccounts(typing.TypedDict):
    newAccount:SolPubkey

def Allocate(
    args: AllocateArgs,
    accounts: AllocateAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["newAccount"], is_signer=True, is_writable=True),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x08\x00\x00\x00"
    encoded_args = layout.build({
        "space":args["space"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



