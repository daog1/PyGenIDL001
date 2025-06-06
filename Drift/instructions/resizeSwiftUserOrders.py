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
class ResizeSwiftUserOrdersArgs(typing.TypedDict):
    numOrders:int


layout = borsh.CStruct(
    "numOrders" /borsh.U16,
    )


class ResizeSwiftUserOrdersAccounts(typing.TypedDict):
    swiftUserOrders:SolPubkey
    authority:SolPubkey
    user:SolPubkey
    systemProgram:SolPubkey

def ResizeSwiftUserOrders(
    args: ResizeSwiftUserOrdersArgs,
    accounts: ResizeSwiftUserOrdersAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["swiftUserOrders"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["authority"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["user"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["systemProgram"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x24\x39\x28\x5a\xc1\x96\xf9\x35"
    encoded_args = layout.build({
        "numOrders":args["numOrders"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)






