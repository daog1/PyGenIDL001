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
class DepositIntoPerpMarketFeePoolArgs(typing.TypedDict):
    amount:int


layout = borsh.CStruct(
    "amount" /borsh.U64,
    )


class DepositIntoPerpMarketFeePoolAccounts(typing.TypedDict):
    state:SolPubkey
    perpMarket:SolPubkey
    admin:SolPubkey
    sourceVault:SolPubkey
    driftSigner:SolPubkey
    quoteSpotMarket:SolPubkey
    spotMarketVault:SolPubkey
    tokenProgram:SolPubkey

def DepositIntoPerpMarketFeePool(
    args: DepositIntoPerpMarketFeePoolArgs,
    accounts: DepositIntoPerpMarketFeePoolAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["state"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["perpMarket"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["admin"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["sourceVault"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["driftSigner"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["quoteSpotMarket"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["spotMarketVault"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenProgram"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x22\x3a\x39\x44\x61\x50\xf4\x06"
    encoded_args = layout.build({
        "amount":args["amount"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)




