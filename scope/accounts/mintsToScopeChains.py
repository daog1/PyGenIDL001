'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from anchorpy.borsh_extension import BorshPubkey
from anchorpy.error import AccountInvalidDiscriminator
from anchorpy.utils.rpc import get_multiple_accounts
from construct import Construct
from dataclasses import dataclass
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Commitment
from solders.pubkey import Pubkey as SolPubkey
from .. import types
from ..program_id import PROGRAM_ID


class MintsToScopeChainsJSON(typing.TypedDict):
    oraclePrices: str
    seedPk: str
    seedId: int
    bump: int
    mapping: list[types.mintToScopeChain.MintToScopeChainJSON]

@dataclass
class MintsToScopeChains:
    #fields
    oraclePrices: SolPubkey
    seedPk: SolPubkey
    seedId: int
    bump: int
    mapping: list[types.mintToScopeChain.MintToScopeChain]

    discriminator: typing.ClassVar = b"\x9c\xec\x38\x14\x27\x8d\x2a\xb7"
    DISCRIMINATOR_SIZE: int = 8

    layout: typing.ClassVar = borsh.CStruct(
        "oraclePrices" /BorshPubkey,
        "seedPk" /BorshPubkey,
        "seedId" /borsh.U64,
        "bump" /borsh.U8,
        "mapping" /borsh.Vec(typing.cast(Construct, types.mintToScopeChain.MintToScopeChain.layout)),
        )



    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: SolPubkey,
        commitment: typing.Optional[Commitment] = None,
        program_id: SolPubkey = PROGRAM_ID,
    ) -> typing.Optional["MintsToScopeChains"]:
        resp = await conn.get_account_info(address, commitment=commitment)
        info = resp.value
        if info is None:
            return None
        if info.owner != program_id:
            raise ValueError("Account does not belong to this program")
        bytes_data = info.data
        return cls.decode(bytes_data)

    @classmethod
    async def fetch_multiple(
        cls,
        conn: AsyncClient,
        addresses: list[SolPubkey],
        commitment: typing.Optional[Commitment] = None,
        program_id: SolPubkey = PROGRAM_ID,
    ) -> typing.List[typing.Optional["MintsToScopeChains"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["MintsToScopeChains"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != program_id:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "MintsToScopeChains":
        if data[:cls.DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = MintsToScopeChains.layout.parse(data[cls.DISCRIMINATOR_SIZE:])
        return cls(
                oraclePrices=dec.oraclePrices,
                seedPk=dec.seedPk,
                seedId=dec.seedId,
                bump=dec.bump,
                mapping=dec.mapping,
                )

    def to_json(self) -> MintsToScopeChainsJSON:
        return {
                "oraclePrices": str(self.oraclePrices),
                "seedPk": str(self.seedPk),
                "seedId": self.seedId,
                "bump": self.bump,
                "mapping": list(map(lambda item:item.to_json(),self.mapping)),
                }

    @classmethod
    def from_json(cls, obj: MintsToScopeChainsJSON) -> "MintsToScopeChains":
        return cls(
                oraclePrices=SolPubkey.from_string(obj["oraclePrices"]),
                seedPk=SolPubkey.from_string(obj["seedPk"]),
                seedId=obj["seedId"],
                bump=obj["bump"],
                mapping=list(map(lambda item:types.mintToScopeChain.MintToScopeChain.from_json(item),obj["mapping"])),
                )




