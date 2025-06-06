'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from construct import Construct
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from .. import types
from ..program_id import PROGRAM_ID
class SharedAccountsRouteArgs(typing.TypedDict):
    id:int
    routePlan:list[types.routePlanStep.RoutePlanStep]
    inAmount:int
    quotedOutAmount:int
    slippageBps:int
    platformFeeBps:int


layout = borsh.CStruct(
    "id" /borsh.U8,
    "routePlan" /borsh.Vec(typing.cast(Construct, types.routePlanStep.RoutePlanStep.layout)),
    "inAmount" /borsh.U64,
    "quotedOutAmount" /borsh.U64,
    "slippageBps" /borsh.U16,
    "platformFeeBps" /borsh.U8,
    )


class SharedAccountsRouteAccounts(typing.TypedDict):
    tokenProgram:SolPubkey
    programAuthority:SolPubkey
    userTransferAuthority:SolPubkey
    sourceTokenAccount:SolPubkey
    programSourceTokenAccount:SolPubkey
    programDestinationTokenAccount:SolPubkey
    destinationTokenAccount:SolPubkey
    sourceMint:SolPubkey
    destinationMint:SolPubkey
    platformFeeAccount:SolPubkey
    token2022Program:SolPubkey
    eventAuthority:SolPubkey
    program:SolPubkey

def SharedAccountsRoute(
    args: SharedAccountsRouteArgs,
    accounts: SharedAccountsRouteAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["tokenProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["programAuthority"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["userTransferAuthority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["sourceTokenAccount"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["programSourceTokenAccount"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["programDestinationTokenAccount"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["destinationTokenAccount"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["sourceMint"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["destinationMint"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["platformFeeAccount"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["token2022Program"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["eventAuthority"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["program"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xc1\x20\x9b\x33\x41\xd6\x9c\x81"
    encoded_args = layout.build({
        "id":args["id"],
        "routePlan":list(map(lambda item:item.to_encodable(),args["routePlan"])),
        "inAmount":args["inAmount"],
        "quotedOutAmount":args["quotedOutAmount"],
        "slippageBps":args["slippageBps"],
        "platformFeeBps":args["platformFeeBps"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)






