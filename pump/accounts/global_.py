'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh;
import typing;
from anchorpy.borsh_extension import BorshPubkey;
from anchorpy.coder.accounts import ACCOUNT_DISCRIMINATOR_SIZE;
from anchorpy.error import AccountInvalidDiscriminator;
from anchorpy.utils.rpc import get_multiple_accounts;
from dataclasses import dataclass;
from solana.rpc.async_api import AsyncClient;
from solana.rpc.commitment import Commitment;
from solana.rpc.types import MemcmpOpts;
from solders.pubkey import Pubkey;
from ..program_id import PROGRAM_ID;


class GlobalJSON(typing.TypedDict):
    initialized: bool
    authority: str
    feeRecipient: str
    initialVirtualTokenReserves: int
    initialVirtualSolReserves: int
    initialRealTokenReserves: int
    tokenTotalSupply: int
    feeBasisPoints: int

@dataclass
class Global:
    discriminator: typing.ClassVar = b"\xa7\xe8\xe8\xb1\xc8\x6c\x72\x7f";

    layout: typing.ClassVar = borsh.CStruct(
        "initialized" /borsh.U8,
        "authority" /BorshPubkey,
        "feeRecipient" /BorshPubkey,
        "initialVirtualTokenReserves" /borsh.U64,
        "initialVirtualSolReserves" /borsh.U64,
        "initialRealTokenReserves" /borsh.U64,
        "tokenTotalSupply" /borsh.U64,
        "feeBasisPoints" /borsh.U64,
        )
    #fields
    initialized: bool
    authority: Pubkey
    feeRecipient: Pubkey
    initialVirtualTokenReserves: int
    initialVirtualSolReserves: int
    initialRealTokenReserves: int
    tokenTotalSupply: int
    feeBasisPoints: int
    

    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: Pubkey,
        commitment: typing.Optional[Commitment] = None,
        program_id: Pubkey = PROGRAM_ID,
    ) -> typing.Optional["Global"]:
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
        addresses: list[Pubkey],
        commitment: typing.Optional[Commitment] = None,
        program_id: Pubkey = PROGRAM_ID,
    ) -> typing.List[typing.Optional["Global"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["Global"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != program_id:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "Global":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = Global.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(
                initialized=dec.initialized,
                authority=dec.authority,
                feeRecipient=dec.feeRecipient,
                initialVirtualTokenReserves=dec.initialVirtualTokenReserves,
                initialVirtualSolReserves=dec.initialVirtualSolReserves,
                initialRealTokenReserves=dec.initialRealTokenReserves,
                tokenTotalSupply=dec.tokenTotalSupply,
                feeBasisPoints=dec.feeBasisPoints,
                )

    def to_json(self) -> GlobalJSON:
        return {
                "initialized": self.initialized,
                "authority": str(self.authority),
                "feeRecipient": str(self.feeRecipient),
                "initialVirtualTokenReserves": self.initialVirtualTokenReserves,
                "initialVirtualSolReserves": self.initialVirtualSolReserves,
                "initialRealTokenReserves": self.initialRealTokenReserves,
                "tokenTotalSupply": self.tokenTotalSupply,
                "feeBasisPoints": self.feeBasisPoints,
                }

    @classmethod
    def from_json(cls, obj: GlobalJSON) -> "Global":
        return cls(
                initialized=obj["initialized"],
                authority=Pubkey.from_string(obj["authority"]),
                feeRecipient=Pubkey.from_string(obj["feeRecipient"]),
                initialVirtualTokenReserves=obj["initialVirtualTokenReserves"],
                initialVirtualSolReserves=obj["initialVirtualSolReserves"],
                initialRealTokenReserves=obj["initialRealTokenReserves"],
                tokenTotalSupply=obj["tokenTotalSupply"],
                feeBasisPoints=obj["feeBasisPoints"],
                )




