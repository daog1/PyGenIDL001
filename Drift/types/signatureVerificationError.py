'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from anchorpy.borsh_extension import EnumForCodegen
from dataclasses import dataclass


class InvalidEd25519InstructionProgramIdJSON(typing.TypedDict):
    kind: typing.Literal["InvalidEd25519InstructionProgramId"]


@dataclass
class InvalidEd25519InstructionProgramId:
    discriminator: typing.ClassVar = 0
    def to_json(self) -> InvalidEd25519InstructionProgramIdJSON:
        return InvalidEd25519InstructionProgramIdJSON(
            kind="InvalidEd25519InstructionProgramId",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "InvalidEd25519InstructionProgramId": {},
        }




class InvalidEd25519InstructionDataLengthJSON(typing.TypedDict):
    kind: typing.Literal["InvalidEd25519InstructionDataLength"]


@dataclass
class InvalidEd25519InstructionDataLength:
    discriminator: typing.ClassVar = 1
    def to_json(self) -> InvalidEd25519InstructionDataLengthJSON:
        return InvalidEd25519InstructionDataLengthJSON(
            kind="InvalidEd25519InstructionDataLength",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "InvalidEd25519InstructionDataLength": {},
        }




class InvalidSignatureIndexJSON(typing.TypedDict):
    kind: typing.Literal["InvalidSignatureIndex"]


@dataclass
class InvalidSignatureIndex:
    discriminator: typing.ClassVar = 2
    def to_json(self) -> InvalidSignatureIndexJSON:
        return InvalidSignatureIndexJSON(
            kind="InvalidSignatureIndex",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "InvalidSignatureIndex": {},
        }




class InvalidSignatureOffsetJSON(typing.TypedDict):
    kind: typing.Literal["InvalidSignatureOffset"]


@dataclass
class InvalidSignatureOffset:
    discriminator: typing.ClassVar = 3
    def to_json(self) -> InvalidSignatureOffsetJSON:
        return InvalidSignatureOffsetJSON(
            kind="InvalidSignatureOffset",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "InvalidSignatureOffset": {},
        }




class InvalidPublicKeyOffsetJSON(typing.TypedDict):
    kind: typing.Literal["InvalidPublicKeyOffset"]


@dataclass
class InvalidPublicKeyOffset:
    discriminator: typing.ClassVar = 4
    def to_json(self) -> InvalidPublicKeyOffsetJSON:
        return InvalidPublicKeyOffsetJSON(
            kind="InvalidPublicKeyOffset",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "InvalidPublicKeyOffset": {},
        }




class InvalidMessageOffsetJSON(typing.TypedDict):
    kind: typing.Literal["InvalidMessageOffset"]


@dataclass
class InvalidMessageOffset:
    discriminator: typing.ClassVar = 5
    def to_json(self) -> InvalidMessageOffsetJSON:
        return InvalidMessageOffsetJSON(
            kind="InvalidMessageOffset",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "InvalidMessageOffset": {},
        }




class InvalidMessageDataSizeJSON(typing.TypedDict):
    kind: typing.Literal["InvalidMessageDataSize"]


@dataclass
class InvalidMessageDataSize:
    discriminator: typing.ClassVar = 6
    def to_json(self) -> InvalidMessageDataSizeJSON:
        return InvalidMessageDataSizeJSON(
            kind="InvalidMessageDataSize",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "InvalidMessageDataSize": {},
        }




class InvalidInstructionIndexJSON(typing.TypedDict):
    kind: typing.Literal["InvalidInstructionIndex"]


@dataclass
class InvalidInstructionIndex:
    discriminator: typing.ClassVar = 7
    def to_json(self) -> InvalidInstructionIndexJSON:
        return InvalidInstructionIndexJSON(
            kind="InvalidInstructionIndex",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "InvalidInstructionIndex": {},
        }




class MessageOffsetOverflowJSON(typing.TypedDict):
    kind: typing.Literal["MessageOffsetOverflow"]


@dataclass
class MessageOffsetOverflow:
    discriminator: typing.ClassVar = 8
    def to_json(self) -> MessageOffsetOverflowJSON:
        return MessageOffsetOverflowJSON(
            kind="MessageOffsetOverflow",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "MessageOffsetOverflow": {},
        }




class InvalidMessageHexJSON(typing.TypedDict):
    kind: typing.Literal["InvalidMessageHex"]


@dataclass
class InvalidMessageHex:
    discriminator: typing.ClassVar = 9
    def to_json(self) -> InvalidMessageHexJSON:
        return InvalidMessageHexJSON(
            kind="InvalidMessageHex",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "InvalidMessageHex": {},
        }





SignatureVerificationErrorKind = typing.Union[
    InvalidEd25519InstructionProgramId,
    InvalidEd25519InstructionDataLength,
    InvalidSignatureIndex,
    InvalidSignatureOffset,
    InvalidPublicKeyOffset,
    InvalidMessageOffset,
    InvalidMessageDataSize,
    InvalidInstructionIndex,
    MessageOffsetOverflow,
    InvalidMessageHex,
]
SignatureVerificationErrorJSON = typing.Union[
    InvalidEd25519InstructionProgramIdJSON,
    InvalidEd25519InstructionDataLengthJSON,
    InvalidSignatureIndexJSON,
    InvalidSignatureOffsetJSON,
    InvalidPublicKeyOffsetJSON,
    InvalidMessageOffsetJSON,
    InvalidMessageDataSizeJSON,
    InvalidInstructionIndexJSON,
    MessageOffsetOverflowJSON,
    InvalidMessageHexJSON,
]

def from_decoded(obj: dict) -> SignatureVerificationErrorKind:
    if not isinstance(obj, dict):
        raise ValueError("Invalid enum object")
    if "InvalidEd25519InstructionProgramId" in obj:
      return InvalidEd25519InstructionProgramId()
    if "InvalidEd25519InstructionDataLength" in obj:
      return InvalidEd25519InstructionDataLength()
    if "InvalidSignatureIndex" in obj:
      return InvalidSignatureIndex()
    if "InvalidSignatureOffset" in obj:
      return InvalidSignatureOffset()
    if "InvalidPublicKeyOffset" in obj:
      return InvalidPublicKeyOffset()
    if "InvalidMessageOffset" in obj:
      return InvalidMessageOffset()
    if "InvalidMessageDataSize" in obj:
      return InvalidMessageDataSize()
    if "InvalidInstructionIndex" in obj:
      return InvalidInstructionIndex()
    if "MessageOffsetOverflow" in obj:
      return MessageOffsetOverflow()
    if "InvalidMessageHex" in obj:
      return InvalidMessageHex()
    raise ValueError("Invalid enum object")

def from_json(obj: SignatureVerificationErrorJSON) -> SignatureVerificationErrorKind:
    if obj["kind"] == "InvalidEd25519InstructionProgramId":
        return InvalidEd25519InstructionProgramId()

    if obj["kind"] == "InvalidEd25519InstructionDataLength":
        return InvalidEd25519InstructionDataLength()

    if obj["kind"] == "InvalidSignatureIndex":
        return InvalidSignatureIndex()

    if obj["kind"] == "InvalidSignatureOffset":
        return InvalidSignatureOffset()

    if obj["kind"] == "InvalidPublicKeyOffset":
        return InvalidPublicKeyOffset()

    if obj["kind"] == "InvalidMessageOffset":
        return InvalidMessageOffset()

    if obj["kind"] == "InvalidMessageDataSize":
        return InvalidMessageDataSize()

    if obj["kind"] == "InvalidInstructionIndex":
        return InvalidInstructionIndex()

    if obj["kind"] == "MessageOffsetOverflow":
        return MessageOffsetOverflow()

    if obj["kind"] == "InvalidMessageHex":
        return InvalidMessageHex()

    kind = obj["kind"]
    raise ValueError(f"Unrecognized enum kind: {kind}")


layout = EnumForCodegen(
"InvalidEd25519InstructionProgramId" / borsh.CStruct(),
"InvalidEd25519InstructionDataLength" / borsh.CStruct(),
"InvalidSignatureIndex" / borsh.CStruct(),
"InvalidSignatureOffset" / borsh.CStruct(),
"InvalidPublicKeyOffset" / borsh.CStruct(),
"InvalidMessageOffset" / borsh.CStruct(),
"InvalidMessageDataSize" / borsh.CStruct(),
"InvalidInstructionIndex" / borsh.CStruct(),
"MessageOffsetOverflow" / borsh.CStruct(),
"InvalidMessageHex" / borsh.CStruct(),
)
