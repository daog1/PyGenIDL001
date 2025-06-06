'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from construct import Container
from dataclasses import dataclass

class AmmConfigJSON(typing.TypedDict):
    lastPrice: int
    lastBalancedPrice: int
    configDenominator: int
    volumeX: int
    volumeY: int
    volumeXInY: int
    depositCap: int
    regressionTarget: int
    oracleType: int
    oracleStatus: int
    oracleMainSlotLimit: int
    oracleSubConfidenceLimit: int
    oracleSubSlotLimit: int
    oraclePcConfidenceLimit: int
    oraclePcSlotLimit: int
    stdSpread: int
    stdSpreadBuffer: int
    spreadCoefficient: int
    priceBufferCoin: int
    priceBufferPc: int
    rebalanceRatio: int
    feeTrade: int
    feePlatform: int
    configTemp3: int
    configTemp4: int
    configTemp5: int
    configTemp6: int
    configTemp7: int
    configTemp8: int

@dataclass
class AmmConfig:
    layout: typing.ClassVar = borsh.CStruct(
        "lastPrice" /borsh.U64,
        "lastBalancedPrice" /borsh.U64,
        "configDenominator" /borsh.U64,
        "volumeX" /borsh.U64,
        "volumeY" /borsh.U64,
        "volumeXInY" /borsh.U64,
        "depositCap" /borsh.U64,
        "regressionTarget" /borsh.U64,
        "oracleType" /borsh.U64,
        "oracleStatus" /borsh.U64,
        "oracleMainSlotLimit" /borsh.U64,
        "oracleSubConfidenceLimit" /borsh.U64,
        "oracleSubSlotLimit" /borsh.U64,
        "oraclePcConfidenceLimit" /borsh.U64,
        "oraclePcSlotLimit" /borsh.U64,
        "stdSpread" /borsh.U64,
        "stdSpreadBuffer" /borsh.U64,
        "spreadCoefficient" /borsh.U64,
        "priceBufferCoin" /borsh.I64,
        "priceBufferPc" /borsh.I64,
        "rebalanceRatio" /borsh.U64,
        "feeTrade" /borsh.U64,
        "feePlatform" /borsh.U64,
        "configTemp3" /borsh.U64,
        "configTemp4" /borsh.U64,
        "configTemp5" /borsh.U64,
        "configTemp6" /borsh.U64,
        "configTemp7" /borsh.U64,
        "configTemp8" /borsh.U64,
        )
    #fields
    lastPrice: int
    lastBalancedPrice: int
    configDenominator: int
    volumeX: int
    volumeY: int
    volumeXInY: int
    depositCap: int
    regressionTarget: int
    oracleType: int
    oracleStatus: int
    oracleMainSlotLimit: int
    oracleSubConfidenceLimit: int
    oracleSubSlotLimit: int
    oraclePcConfidenceLimit: int
    oraclePcSlotLimit: int
    stdSpread: int
    stdSpreadBuffer: int
    spreadCoefficient: int
    priceBufferCoin: int
    priceBufferPc: int
    rebalanceRatio: int
    feeTrade: int
    feePlatform: int
    configTemp3: int
    configTemp4: int
    configTemp5: int
    configTemp6: int
    configTemp7: int
    configTemp8: int
    
    @classmethod
    def from_decoded(cls, obj: Container) -> "AmmConfig":
        return cls(
        lastPrice=obj["lastPrice"],
        lastBalancedPrice=obj["lastBalancedPrice"],
        configDenominator=obj["configDenominator"],
        volumeX=obj["volumeX"],
        volumeY=obj["volumeY"],
        volumeXInY=obj["volumeXInY"],
        depositCap=obj["depositCap"],
        regressionTarget=obj["regressionTarget"],
        oracleType=obj["oracleType"],
        oracleStatus=obj["oracleStatus"],
        oracleMainSlotLimit=obj["oracleMainSlotLimit"],
        oracleSubConfidenceLimit=obj["oracleSubConfidenceLimit"],
        oracleSubSlotLimit=obj["oracleSubSlotLimit"],
        oraclePcConfidenceLimit=obj["oraclePcConfidenceLimit"],
        oraclePcSlotLimit=obj["oraclePcSlotLimit"],
        stdSpread=obj["stdSpread"],
        stdSpreadBuffer=obj["stdSpreadBuffer"],
        spreadCoefficient=obj["spreadCoefficient"],
        priceBufferCoin=obj["priceBufferCoin"],
        priceBufferPc=obj["priceBufferPc"],
        rebalanceRatio=obj["rebalanceRatio"],
        feeTrade=obj["feeTrade"],
        feePlatform=obj["feePlatform"],
        configTemp3=obj["configTemp3"],
        configTemp4=obj["configTemp4"],
        configTemp5=obj["configTemp5"],
        configTemp6=obj["configTemp6"],
        configTemp7=obj["configTemp7"],
        configTemp8=obj["configTemp8"],
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
                "lastPrice": self.lastPrice,
                "lastBalancedPrice": self.lastBalancedPrice,
                "configDenominator": self.configDenominator,
                "volumeX": self.volumeX,
                "volumeY": self.volumeY,
                "volumeXInY": self.volumeXInY,
                "depositCap": self.depositCap,
                "regressionTarget": self.regressionTarget,
                "oracleType": self.oracleType,
                "oracleStatus": self.oracleStatus,
                "oracleMainSlotLimit": self.oracleMainSlotLimit,
                "oracleSubConfidenceLimit": self.oracleSubConfidenceLimit,
                "oracleSubSlotLimit": self.oracleSubSlotLimit,
                "oraclePcConfidenceLimit": self.oraclePcConfidenceLimit,
                "oraclePcSlotLimit": self.oraclePcSlotLimit,
                "stdSpread": self.stdSpread,
                "stdSpreadBuffer": self.stdSpreadBuffer,
                "spreadCoefficient": self.spreadCoefficient,
                "priceBufferCoin": self.priceBufferCoin,
                "priceBufferPc": self.priceBufferPc,
                "rebalanceRatio": self.rebalanceRatio,
                "feeTrade": self.feeTrade,
                "feePlatform": self.feePlatform,
                "configTemp3": self.configTemp3,
                "configTemp4": self.configTemp4,
                "configTemp5": self.configTemp5,
                "configTemp6": self.configTemp6,
                "configTemp7": self.configTemp7,
                "configTemp8": self.configTemp8,
                }

    def to_json(self) -> AmmConfigJSON:
        return {
                "lastPrice": self.lastPrice,
                "lastBalancedPrice": self.lastBalancedPrice,
                "configDenominator": self.configDenominator,
                "volumeX": self.volumeX,
                "volumeY": self.volumeY,
                "volumeXInY": self.volumeXInY,
                "depositCap": self.depositCap,
                "regressionTarget": self.regressionTarget,
                "oracleType": self.oracleType,
                "oracleStatus": self.oracleStatus,
                "oracleMainSlotLimit": self.oracleMainSlotLimit,
                "oracleSubConfidenceLimit": self.oracleSubConfidenceLimit,
                "oracleSubSlotLimit": self.oracleSubSlotLimit,
                "oraclePcConfidenceLimit": self.oraclePcConfidenceLimit,
                "oraclePcSlotLimit": self.oraclePcSlotLimit,
                "stdSpread": self.stdSpread,
                "stdSpreadBuffer": self.stdSpreadBuffer,
                "spreadCoefficient": self.spreadCoefficient,
                "priceBufferCoin": self.priceBufferCoin,
                "priceBufferPc": self.priceBufferPc,
                "rebalanceRatio": self.rebalanceRatio,
                "feeTrade": self.feeTrade,
                "feePlatform": self.feePlatform,
                "configTemp3": self.configTemp3,
                "configTemp4": self.configTemp4,
                "configTemp5": self.configTemp5,
                "configTemp6": self.configTemp6,
                "configTemp7": self.configTemp7,
                "configTemp8": self.configTemp8,
                }

    @classmethod
    def from_json(cls, obj: AmmConfigJSON) -> "AmmConfig":
        return cls(
                lastPrice=obj["lastPrice"],
                lastBalancedPrice=obj["lastBalancedPrice"],
                configDenominator=obj["configDenominator"],
                volumeX=obj["volumeX"],
                volumeY=obj["volumeY"],
                volumeXInY=obj["volumeXInY"],
                depositCap=obj["depositCap"],
                regressionTarget=obj["regressionTarget"],
                oracleType=obj["oracleType"],
                oracleStatus=obj["oracleStatus"],
                oracleMainSlotLimit=obj["oracleMainSlotLimit"],
                oracleSubConfidenceLimit=obj["oracleSubConfidenceLimit"],
                oracleSubSlotLimit=obj["oracleSubSlotLimit"],
                oraclePcConfidenceLimit=obj["oraclePcConfidenceLimit"],
                oraclePcSlotLimit=obj["oraclePcSlotLimit"],
                stdSpread=obj["stdSpread"],
                stdSpreadBuffer=obj["stdSpreadBuffer"],
                spreadCoefficient=obj["spreadCoefficient"],
                priceBufferCoin=obj["priceBufferCoin"],
                priceBufferPc=obj["priceBufferPc"],
                rebalanceRatio=obj["rebalanceRatio"],
                feeTrade=obj["feeTrade"],
                feePlatform=obj["feePlatform"],
                configTemp3=obj["configTemp3"],
                configTemp4=obj["configTemp4"],
                configTemp5=obj["configTemp5"],
                configTemp6=obj["configTemp6"],
                configTemp7=obj["configTemp7"],
                configTemp8=obj["configTemp8"],
        )






