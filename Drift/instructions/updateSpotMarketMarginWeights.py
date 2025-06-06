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
class UpdateSpotMarketMarginWeightsArgs(typing.TypedDict):
    initialAssetWeight:int
    maintenanceAssetWeight:int
    initialLiabilityWeight:int
    maintenanceLiabilityWeight:int
    imfFactor:int


layout = borsh.CStruct(
    "initialAssetWeight" /borsh.U32,
    "maintenanceAssetWeight" /borsh.U32,
    "initialLiabilityWeight" /borsh.U32,
    "maintenanceLiabilityWeight" /borsh.U32,
    "imfFactor" /borsh.U32,
    )


class UpdateSpotMarketMarginWeightsAccounts(typing.TypedDict):
    admin:SolPubkey
    state:SolPubkey
    spotMarket:SolPubkey

def UpdateSpotMarketMarginWeights(
    args: UpdateSpotMarketMarginWeightsArgs,
    accounts: UpdateSpotMarketMarginWeightsAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["admin"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["state"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["spotMarket"], is_signer=False, is_writable=True),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x6d\x21\x57\xc3\xff\x24\x06\x51"
    encoded_args = layout.build({
        "initialAssetWeight":args["initialAssetWeight"],
        "maintenanceAssetWeight":args["maintenanceAssetWeight"],
        "initialLiabilityWeight":args["initialLiabilityWeight"],
        "maintenanceLiabilityWeight":args["maintenanceLiabilityWeight"],
        "imfFactor":args["imfFactor"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



