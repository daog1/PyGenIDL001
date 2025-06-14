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
from .. import types
from ..program_id import TOKEN_2022_PROGRAM_ADDRESS
class UpdateTokenMetadataFieldArgs(typing.TypedDict):
    field:types.tokenMetadataField.TokenMetadataFieldKind
    value:str


layout = borsh.CStruct(
    "field" /types.tokenMetadataField.layout,
    "value" /borsh.String,
    )


class UpdateTokenMetadataFieldAccounts(typing.TypedDict):
    metadata:SolPubkey
    updateAuthority:SolPubkey

def UpdateTokenMetadataField(
    args: UpdateTokenMetadataFieldArgs,
    accounts: UpdateTokenMetadataFieldAccounts,
    program_id: SolPubkey =  TOKEN_2022_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["metadata"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["updateAuthority"], is_signer=True, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    encoded_args = layout.build({
        "field":args["field"].to_encodable(),
        "value":args["value"],
       })
    return Instruction(program_id,encoded_args,keys)



