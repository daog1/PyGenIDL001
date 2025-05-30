'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh;
import typing;
from construct import Container;
from dataclasses import dataclass;
from solders.instruction import AccountMeta, Instruction;
from solders.pubkey import Pubkey as SolPubkey;
from solders.sysvar import RENT;
from ..program_id import PROGRAM_ID;

class UpdateUserQuoteAssetInsuranceStakeAccounts(typing.TypedDict):
    state:SolPubkey
    spotMarket:SolPubkey
    insuranceFundStake:SolPubkey
    userStats:SolPubkey
    signer:SolPubkey
    insuranceFundVault:SolPubkey

def UpdateUserQuoteAssetInsuranceStake(
    accounts: UpdateUserQuoteAssetInsuranceStakeAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["state"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["spotMarket"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["insuranceFundStake"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["userStats"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["signer"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["insuranceFundVault"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=RENT, is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xfb\x65\x9c\x07\x02\x3f\x1e\x17"
    encoded_args = b""

    data = identifier + encoded_args
    return Instruction(program_id,data,keys)


