'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from anchorpy.borsh_extension import BorshPubkey
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import PROGRAM_ID
class AuthorizeNonceAccountArgs(typing.TypedDict):
    newNonceAuthority:SolPubkey


layout = borsh.CStruct(
    "newNonceAuthority" /BorshPubkey,
    )


class AuthorizeNonceAccountAccounts(typing.TypedDict):
    nonceAccount:SolPubkey
    nonceAuthority:SolPubkey

def AuthorizeNonceAccount(
    args: AuthorizeNonceAccountArgs,
    accounts: AuthorizeNonceAccountAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["nonceAccount"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["nonceAuthority"], is_signer=True, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x07\x00\x00\x00"
    encoded_args = layout.build({
        "newNonceAuthority":args["newNonceAuthority"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



