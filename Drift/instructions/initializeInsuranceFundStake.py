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
class InitializeInsuranceFundStakeArgs(typing.TypedDict):
    marketIndex:int


layout = borsh.CStruct(
    "marketIndex" /borsh.U16,
    )


class InitializeInsuranceFundStakeAccounts(typing.TypedDict):
    spotMarket:SolPubkey
    insuranceFundStake:SolPubkey
    userStats:SolPubkey
    state:SolPubkey
    authority:SolPubkey
    payer:SolPubkey
    rent:SolPubkey
    systemProgram:SolPubkey

def InitializeInsuranceFundStake(
    args: InitializeInsuranceFundStakeArgs,
    accounts: InitializeInsuranceFundStakeAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["spotMarket"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["insuranceFundStake"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["userStats"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["state"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["authority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["systemProgram"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xbb\xb3\xf3\x46\xf8\x5a\x5c\x93"
    encoded_args = layout.build({
        "marketIndex":args["marketIndex"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)










