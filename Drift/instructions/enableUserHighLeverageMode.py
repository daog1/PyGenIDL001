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
class EnableUserHighLeverageModeArgs(typing.TypedDict):
    subAccountId:int


layout = borsh.CStruct(
    "subAccountId" /borsh.U16,
    )


class EnableUserHighLeverageModeAccounts(typing.TypedDict):
    state:SolPubkey
    user:SolPubkey
    authority:SolPubkey
    highLeverageModeConfig:SolPubkey

def EnableUserHighLeverageMode(
    args: EnableUserHighLeverageModeArgs,
    accounts: EnableUserHighLeverageModeAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["state"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["user"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["authority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["highLeverageModeConfig"], is_signer=False, is_writable=True),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xe7\x18\xe6\x70\xc9\xad\x49\xb8"
    encoded_args = layout.build({
        "subAccountId":args["subAccountId"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)




