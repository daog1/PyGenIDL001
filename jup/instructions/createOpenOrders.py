'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import PROGRAM_ID

class CreateOpenOrdersAccounts(typing.TypedDict):
    openOrders:SolPubkey
    payer:SolPubkey
    dexProgram:SolPubkey
    systemProgram:SolPubkey
    rent:SolPubkey
    market:SolPubkey

def CreateOpenOrders(
    accounts: CreateOpenOrdersAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["openOrders"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["dexProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["systemProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["market"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xe5\xc2\xd4\xac\x08\x0a\x86\x93"
    encoded_args = b""
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)


def find_OpenOrders(market: SolPubkey, payer: SolPubkey) -> typing.Tuple[SolPubkey, int]:
    seeds = [
       b"\x6f\x70\x65\x6e\x5f\x6f\x72\x64\x65\x72\x73",
       bytes(market),
       bytes(payer),
    ]

    address, bump = SolPubkey.find_program_address(seeds,
        PROGRAM_ID
            )

    return address, bump









