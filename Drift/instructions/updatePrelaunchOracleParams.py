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
from ..program_id import PROGRAM_ID
class UpdatePrelaunchOracleParamsArgs(typing.TypedDict):
    params:types.prelaunchOracleParams.PrelaunchOracleParams


layout = borsh.CStruct(
    "params" /types.prelaunchOracleParams.PrelaunchOracleParams.layout,
    )


class UpdatePrelaunchOracleParamsAccounts(typing.TypedDict):
    admin:SolPubkey
    prelaunchOracle:SolPubkey
    perpMarket:SolPubkey
    state:SolPubkey

def UpdatePrelaunchOracleParams(
    args: UpdatePrelaunchOracleParamsArgs,
    accounts: UpdatePrelaunchOracleParamsAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["admin"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["prelaunchOracle"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["perpMarket"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["state"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x62\xcd\x93\xf3\x12\x4b\x53\xcf"
    encoded_args = layout.build({
        "params":args["params"].to_encodable(),
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



