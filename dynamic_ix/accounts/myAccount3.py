'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from anchorpy.error import AccountInvalidDiscriminator
from anchorpy.utils.rpc import get_multiple_accounts
from dataclasses import dataclass
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Commitment
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import PROGRAM_ID


class MyAccount3JSON(typing.TypedDict):
    field: int

@dataclass
class MyAccount3:
    #fields
    field: int

    discriminator: typing.ClassVar = b"\x03\x00"
    DISCRIMINATOR_SIZE: int = 2

    layout: typing.ClassVar = borsh.CStruct(
        "field" /borsh.U8,
        )



    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: SolPubkey,
        commitment: typing.Optional[Commitment] = None,
        program_id: SolPubkey = PROGRAM_ID,
    ) -> typing.Optional["MyAccount3"]:
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
    ) -> typing.List[typing.Optional["MyAccount3"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["MyAccount3"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != program_id:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "MyAccount3":
        if data[:cls.DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = MyAccount3.layout.parse(data[cls.DISCRIMINATOR_SIZE:])
        return cls(
                field=dec.field,
                )

    def to_json(self) -> MyAccount3JSON:
        return {
                "field": self.field,
                }

    @classmethod
    def from_json(cls, obj: MyAccount3JSON) -> "MyAccount3":
        return cls(
                field=obj["field"],
                )




