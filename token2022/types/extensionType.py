'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from dataclasses import dataclass
from ..shared import EnumForCodegenU16


class UninitializedJSON(typing.TypedDict):
    kind: typing.Literal["Uninitialized"]


@dataclass
class Uninitialized:
    discriminator: typing.ClassVar = 0
    def to_json(self) -> UninitializedJSON:
        return UninitializedJSON(
            kind="Uninitialized",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "Uninitialized": {},
        }




class TransferFeeConfigJSON(typing.TypedDict):
    kind: typing.Literal["TransferFeeConfig"]


@dataclass
class TransferFeeConfig:
    discriminator: typing.ClassVar = 1
    def to_json(self) -> TransferFeeConfigJSON:
        return TransferFeeConfigJSON(
            kind="TransferFeeConfig",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "TransferFeeConfig": {},
        }




class TransferFeeAmountJSON(typing.TypedDict):
    kind: typing.Literal["TransferFeeAmount"]


@dataclass
class TransferFeeAmount:
    discriminator: typing.ClassVar = 2
    def to_json(self) -> TransferFeeAmountJSON:
        return TransferFeeAmountJSON(
            kind="TransferFeeAmount",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "TransferFeeAmount": {},
        }




class MintCloseAuthorityJSON(typing.TypedDict):
    kind: typing.Literal["MintCloseAuthority"]


@dataclass
class MintCloseAuthority:
    discriminator: typing.ClassVar = 3
    def to_json(self) -> MintCloseAuthorityJSON:
        return MintCloseAuthorityJSON(
            kind="MintCloseAuthority",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "MintCloseAuthority": {},
        }




class ConfidentialTransferMintJSON(typing.TypedDict):
    kind: typing.Literal["ConfidentialTransferMint"]


@dataclass
class ConfidentialTransferMint:
    discriminator: typing.ClassVar = 4
    def to_json(self) -> ConfidentialTransferMintJSON:
        return ConfidentialTransferMintJSON(
            kind="ConfidentialTransferMint",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "ConfidentialTransferMint": {},
        }




class ConfidentialTransferAccountJSON(typing.TypedDict):
    kind: typing.Literal["ConfidentialTransferAccount"]


@dataclass
class ConfidentialTransferAccount:
    discriminator: typing.ClassVar = 5
    def to_json(self) -> ConfidentialTransferAccountJSON:
        return ConfidentialTransferAccountJSON(
            kind="ConfidentialTransferAccount",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "ConfidentialTransferAccount": {},
        }




class DefaultAccountStateJSON(typing.TypedDict):
    kind: typing.Literal["DefaultAccountState"]


@dataclass
class DefaultAccountState:
    discriminator: typing.ClassVar = 6
    def to_json(self) -> DefaultAccountStateJSON:
        return DefaultAccountStateJSON(
            kind="DefaultAccountState",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "DefaultAccountState": {},
        }




class ImmutableOwnerJSON(typing.TypedDict):
    kind: typing.Literal["ImmutableOwner"]


@dataclass
class ImmutableOwner:
    discriminator: typing.ClassVar = 7
    def to_json(self) -> ImmutableOwnerJSON:
        return ImmutableOwnerJSON(
            kind="ImmutableOwner",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "ImmutableOwner": {},
        }




class MemoTransferJSON(typing.TypedDict):
    kind: typing.Literal["MemoTransfer"]


@dataclass
class MemoTransfer:
    discriminator: typing.ClassVar = 8
    def to_json(self) -> MemoTransferJSON:
        return MemoTransferJSON(
            kind="MemoTransfer",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "MemoTransfer": {},
        }




class NonTransferableJSON(typing.TypedDict):
    kind: typing.Literal["NonTransferable"]


@dataclass
class NonTransferable:
    discriminator: typing.ClassVar = 9
    def to_json(self) -> NonTransferableJSON:
        return NonTransferableJSON(
            kind="NonTransferable",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "NonTransferable": {},
        }




class InterestBearingConfigJSON(typing.TypedDict):
    kind: typing.Literal["InterestBearingConfig"]


@dataclass
class InterestBearingConfig:
    discriminator: typing.ClassVar = 10
    def to_json(self) -> InterestBearingConfigJSON:
        return InterestBearingConfigJSON(
            kind="InterestBearingConfig",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "InterestBearingConfig": {},
        }




class CpiGuardJSON(typing.TypedDict):
    kind: typing.Literal["CpiGuard"]


@dataclass
class CpiGuard:
    discriminator: typing.ClassVar = 11
    def to_json(self) -> CpiGuardJSON:
        return CpiGuardJSON(
            kind="CpiGuard",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "CpiGuard": {},
        }




class PermanentDelegateJSON(typing.TypedDict):
    kind: typing.Literal["PermanentDelegate"]


@dataclass
class PermanentDelegate:
    discriminator: typing.ClassVar = 12
    def to_json(self) -> PermanentDelegateJSON:
        return PermanentDelegateJSON(
            kind="PermanentDelegate",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "PermanentDelegate": {},
        }




class NonTransferableAccountJSON(typing.TypedDict):
    kind: typing.Literal["NonTransferableAccount"]


@dataclass
class NonTransferableAccount:
    discriminator: typing.ClassVar = 13
    def to_json(self) -> NonTransferableAccountJSON:
        return NonTransferableAccountJSON(
            kind="NonTransferableAccount",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "NonTransferableAccount": {},
        }




class TransferHookJSON(typing.TypedDict):
    kind: typing.Literal["TransferHook"]


@dataclass
class TransferHook:
    discriminator: typing.ClassVar = 14
    def to_json(self) -> TransferHookJSON:
        return TransferHookJSON(
            kind="TransferHook",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "TransferHook": {},
        }




class TransferHookAccountJSON(typing.TypedDict):
    kind: typing.Literal["TransferHookAccount"]


@dataclass
class TransferHookAccount:
    discriminator: typing.ClassVar = 15
    def to_json(self) -> TransferHookAccountJSON:
        return TransferHookAccountJSON(
            kind="TransferHookAccount",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "TransferHookAccount": {},
        }




class ConfidentialTransferFeeJSON(typing.TypedDict):
    kind: typing.Literal["ConfidentialTransferFee"]


@dataclass
class ConfidentialTransferFee:
    discriminator: typing.ClassVar = 16
    def to_json(self) -> ConfidentialTransferFeeJSON:
        return ConfidentialTransferFeeJSON(
            kind="ConfidentialTransferFee",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "ConfidentialTransferFee": {},
        }




class ConfidentialTransferFeeAmountJSON(typing.TypedDict):
    kind: typing.Literal["ConfidentialTransferFeeAmount"]


@dataclass
class ConfidentialTransferFeeAmount:
    discriminator: typing.ClassVar = 17
    def to_json(self) -> ConfidentialTransferFeeAmountJSON:
        return ConfidentialTransferFeeAmountJSON(
            kind="ConfidentialTransferFeeAmount",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "ConfidentialTransferFeeAmount": {},
        }




class ScaledUiAmountConfigJSON(typing.TypedDict):
    kind: typing.Literal["ScaledUiAmountConfig"]


@dataclass
class ScaledUiAmountConfig:
    discriminator: typing.ClassVar = 18
    def to_json(self) -> ScaledUiAmountConfigJSON:
        return ScaledUiAmountConfigJSON(
            kind="ScaledUiAmountConfig",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "ScaledUiAmountConfig": {},
        }




class PausableConfigJSON(typing.TypedDict):
    kind: typing.Literal["PausableConfig"]


@dataclass
class PausableConfig:
    discriminator: typing.ClassVar = 19
    def to_json(self) -> PausableConfigJSON:
        return PausableConfigJSON(
            kind="PausableConfig",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "PausableConfig": {},
        }




class PausableAccountJSON(typing.TypedDict):
    kind: typing.Literal["PausableAccount"]


@dataclass
class PausableAccount:
    discriminator: typing.ClassVar = 20
    def to_json(self) -> PausableAccountJSON:
        return PausableAccountJSON(
            kind="PausableAccount",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "PausableAccount": {},
        }




class MetadataPointerJSON(typing.TypedDict):
    kind: typing.Literal["MetadataPointer"]


@dataclass
class MetadataPointer:
    discriminator: typing.ClassVar = 21
    def to_json(self) -> MetadataPointerJSON:
        return MetadataPointerJSON(
            kind="MetadataPointer",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "MetadataPointer": {},
        }




class TokenMetadataJSON(typing.TypedDict):
    kind: typing.Literal["TokenMetadata"]


@dataclass
class TokenMetadata:
    discriminator: typing.ClassVar = 22
    def to_json(self) -> TokenMetadataJSON:
        return TokenMetadataJSON(
            kind="TokenMetadata",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "TokenMetadata": {},
        }




class GroupPointerJSON(typing.TypedDict):
    kind: typing.Literal["GroupPointer"]


@dataclass
class GroupPointer:
    discriminator: typing.ClassVar = 23
    def to_json(self) -> GroupPointerJSON:
        return GroupPointerJSON(
            kind="GroupPointer",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "GroupPointer": {},
        }




class TokenGroupJSON(typing.TypedDict):
    kind: typing.Literal["TokenGroup"]


@dataclass
class TokenGroup:
    discriminator: typing.ClassVar = 24
    def to_json(self) -> TokenGroupJSON:
        return TokenGroupJSON(
            kind="TokenGroup",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "TokenGroup": {},
        }




class GroupMemberPointerJSON(typing.TypedDict):
    kind: typing.Literal["GroupMemberPointer"]


@dataclass
class GroupMemberPointer:
    discriminator: typing.ClassVar = 25
    def to_json(self) -> GroupMemberPointerJSON:
        return GroupMemberPointerJSON(
            kind="GroupMemberPointer",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "GroupMemberPointer": {},
        }




class TokenGroupMemberJSON(typing.TypedDict):
    kind: typing.Literal["TokenGroupMember"]


@dataclass
class TokenGroupMember:
    discriminator: typing.ClassVar = 26
    def to_json(self) -> TokenGroupMemberJSON:
        return TokenGroupMemberJSON(
            kind="TokenGroupMember",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "TokenGroupMember": {},
        }





ExtensionTypeKind = typing.Union[
    Uninitialized,
    TransferFeeConfig,
    TransferFeeAmount,
    MintCloseAuthority,
    ConfidentialTransferMint,
    ConfidentialTransferAccount,
    DefaultAccountState,
    ImmutableOwner,
    MemoTransfer,
    NonTransferable,
    InterestBearingConfig,
    CpiGuard,
    PermanentDelegate,
    NonTransferableAccount,
    TransferHook,
    TransferHookAccount,
    ConfidentialTransferFee,
    ConfidentialTransferFeeAmount,
    ScaledUiAmountConfig,
    PausableConfig,
    PausableAccount,
    MetadataPointer,
    TokenMetadata,
    GroupPointer,
    TokenGroup,
    GroupMemberPointer,
    TokenGroupMember,
]
ExtensionTypeJSON = typing.Union[
    UninitializedJSON,
    TransferFeeConfigJSON,
    TransferFeeAmountJSON,
    MintCloseAuthorityJSON,
    ConfidentialTransferMintJSON,
    ConfidentialTransferAccountJSON,
    DefaultAccountStateJSON,
    ImmutableOwnerJSON,
    MemoTransferJSON,
    NonTransferableJSON,
    InterestBearingConfigJSON,
    CpiGuardJSON,
    PermanentDelegateJSON,
    NonTransferableAccountJSON,
    TransferHookJSON,
    TransferHookAccountJSON,
    ConfidentialTransferFeeJSON,
    ConfidentialTransferFeeAmountJSON,
    ScaledUiAmountConfigJSON,
    PausableConfigJSON,
    PausableAccountJSON,
    MetadataPointerJSON,
    TokenMetadataJSON,
    GroupPointerJSON,
    TokenGroupJSON,
    GroupMemberPointerJSON,
    TokenGroupMemberJSON,
]

def from_decoded(obj: dict) -> ExtensionTypeKind:
    if not isinstance(obj, dict):
        raise ValueError("Invalid enum object")
    if "Uninitialized" in obj:
      return Uninitialized()
    if "TransferFeeConfig" in obj:
      return TransferFeeConfig()
    if "TransferFeeAmount" in obj:
      return TransferFeeAmount()
    if "MintCloseAuthority" in obj:
      return MintCloseAuthority()
    if "ConfidentialTransferMint" in obj:
      return ConfidentialTransferMint()
    if "ConfidentialTransferAccount" in obj:
      return ConfidentialTransferAccount()
    if "DefaultAccountState" in obj:
      return DefaultAccountState()
    if "ImmutableOwner" in obj:
      return ImmutableOwner()
    if "MemoTransfer" in obj:
      return MemoTransfer()
    if "NonTransferable" in obj:
      return NonTransferable()
    if "InterestBearingConfig" in obj:
      return InterestBearingConfig()
    if "CpiGuard" in obj:
      return CpiGuard()
    if "PermanentDelegate" in obj:
      return PermanentDelegate()
    if "NonTransferableAccount" in obj:
      return NonTransferableAccount()
    if "TransferHook" in obj:
      return TransferHook()
    if "TransferHookAccount" in obj:
      return TransferHookAccount()
    if "ConfidentialTransferFee" in obj:
      return ConfidentialTransferFee()
    if "ConfidentialTransferFeeAmount" in obj:
      return ConfidentialTransferFeeAmount()
    if "ScaledUiAmountConfig" in obj:
      return ScaledUiAmountConfig()
    if "PausableConfig" in obj:
      return PausableConfig()
    if "PausableAccount" in obj:
      return PausableAccount()
    if "MetadataPointer" in obj:
      return MetadataPointer()
    if "TokenMetadata" in obj:
      return TokenMetadata()
    if "GroupPointer" in obj:
      return GroupPointer()
    if "TokenGroup" in obj:
      return TokenGroup()
    if "GroupMemberPointer" in obj:
      return GroupMemberPointer()
    if "TokenGroupMember" in obj:
      return TokenGroupMember()
    raise ValueError("Invalid enum object")

def from_json(obj: ExtensionTypeJSON) -> ExtensionTypeKind:
    if obj["kind"] == "Uninitialized":
        return Uninitialized()

    if obj["kind"] == "TransferFeeConfig":
        return TransferFeeConfig()

    if obj["kind"] == "TransferFeeAmount":
        return TransferFeeAmount()

    if obj["kind"] == "MintCloseAuthority":
        return MintCloseAuthority()

    if obj["kind"] == "ConfidentialTransferMint":
        return ConfidentialTransferMint()

    if obj["kind"] == "ConfidentialTransferAccount":
        return ConfidentialTransferAccount()

    if obj["kind"] == "DefaultAccountState":
        return DefaultAccountState()

    if obj["kind"] == "ImmutableOwner":
        return ImmutableOwner()

    if obj["kind"] == "MemoTransfer":
        return MemoTransfer()

    if obj["kind"] == "NonTransferable":
        return NonTransferable()

    if obj["kind"] == "InterestBearingConfig":
        return InterestBearingConfig()

    if obj["kind"] == "CpiGuard":
        return CpiGuard()

    if obj["kind"] == "PermanentDelegate":
        return PermanentDelegate()

    if obj["kind"] == "NonTransferableAccount":
        return NonTransferableAccount()

    if obj["kind"] == "TransferHook":
        return TransferHook()

    if obj["kind"] == "TransferHookAccount":
        return TransferHookAccount()

    if obj["kind"] == "ConfidentialTransferFee":
        return ConfidentialTransferFee()

    if obj["kind"] == "ConfidentialTransferFeeAmount":
        return ConfidentialTransferFeeAmount()

    if obj["kind"] == "ScaledUiAmountConfig":
        return ScaledUiAmountConfig()

    if obj["kind"] == "PausableConfig":
        return PausableConfig()

    if obj["kind"] == "PausableAccount":
        return PausableAccount()

    if obj["kind"] == "MetadataPointer":
        return MetadataPointer()

    if obj["kind"] == "TokenMetadata":
        return TokenMetadata()

    if obj["kind"] == "GroupPointer":
        return GroupPointer()

    if obj["kind"] == "TokenGroup":
        return TokenGroup()

    if obj["kind"] == "GroupMemberPointer":
        return GroupMemberPointer()

    if obj["kind"] == "TokenGroupMember":
        return TokenGroupMember()

    kind = obj["kind"]
    raise ValueError(f"Unrecognized enum kind: {kind}")


layout = EnumForCodegenU16(
"Uninitialized" / borsh.CStruct(),
"TransferFeeConfig" / borsh.CStruct(),
"TransferFeeAmount" / borsh.CStruct(),
"MintCloseAuthority" / borsh.CStruct(),
"ConfidentialTransferMint" / borsh.CStruct(),
"ConfidentialTransferAccount" / borsh.CStruct(),
"DefaultAccountState" / borsh.CStruct(),
"ImmutableOwner" / borsh.CStruct(),
"MemoTransfer" / borsh.CStruct(),
"NonTransferable" / borsh.CStruct(),
"InterestBearingConfig" / borsh.CStruct(),
"CpiGuard" / borsh.CStruct(),
"PermanentDelegate" / borsh.CStruct(),
"NonTransferableAccount" / borsh.CStruct(),
"TransferHook" / borsh.CStruct(),
"TransferHookAccount" / borsh.CStruct(),
"ConfidentialTransferFee" / borsh.CStruct(),
"ConfidentialTransferFeeAmount" / borsh.CStruct(),
"ScaledUiAmountConfig" / borsh.CStruct(),
"PausableConfig" / borsh.CStruct(),
"PausableAccount" / borsh.CStruct(),
"MetadataPointer" / borsh.CStruct(),
"TokenMetadata" / borsh.CStruct(),
"GroupPointer" / borsh.CStruct(),
"TokenGroup" / borsh.CStruct(),
"GroupMemberPointer" / borsh.CStruct(),
"TokenGroupMember" / borsh.CStruct(),
)
