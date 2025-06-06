'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

from . import aMM
from .aMM import AMMJSON,AMM;
from . import aMMAvailability
from .aMMAvailability import AMMAvailabilityJSON,AMMAvailabilityKind;
from . import aMMLiquiditySplit
from .aMMLiquiditySplit import AMMLiquiditySplitJSON,AMMLiquiditySplitKind;
from . import assetTier
from .assetTier import AssetTierJSON,AssetTierKind;
from . import assetType
from .assetType import AssetTypeJSON,AssetTypeKind;
from . import contractTier
from .contractTier import ContractTierJSON,ContractTierKind;
from . import contractType
from .contractType import ContractTypeJSON,ContractTypeKind;
from . import depositDirection
from .depositDirection import DepositDirectionJSON,DepositDirectionKind;
from . import depositExplanation
from .depositExplanation import DepositExplanationJSON,DepositExplanationKind;
from . import driftAction
from .driftAction import DriftActionJSON,DriftActionKind;
from . import exchangeStatus
from .exchangeStatus import ExchangeStatusJSON,ExchangeStatusKind;
from . import feeStructure
from .feeStructure import FeeStructureJSON,FeeStructure;
from . import feeTier
from .feeTier import FeeTierJSON,FeeTier;
from . import fillMode
from .fillMode import FillModeJSON,FillModeKind;
from . import historicalIndexData
from .historicalIndexData import HistoricalIndexDataJSON,HistoricalIndexData;
from . import historicalOracleData
from .historicalOracleData import HistoricalOracleDataJSON,HistoricalOracleData;
from . import insuranceClaim
from .insuranceClaim import InsuranceClaimJSON,InsuranceClaim;
from . import insuranceFund
from .insuranceFund import InsuranceFundJSON,InsuranceFund;
from . import insuranceFundOperation
from .insuranceFundOperation import InsuranceFundOperationJSON,InsuranceFundOperationKind;
from . import liquidateBorrowForPerpPnlRecord
from .liquidateBorrowForPerpPnlRecord import LiquidateBorrowForPerpPnlRecordJSON,LiquidateBorrowForPerpPnlRecord;
from . import liquidatePerpPnlForDepositRecord
from .liquidatePerpPnlForDepositRecord import LiquidatePerpPnlForDepositRecordJSON,LiquidatePerpPnlForDepositRecord;
from . import liquidatePerpRecord
from .liquidatePerpRecord import LiquidatePerpRecordJSON,LiquidatePerpRecord;
from . import liquidateSpotRecord
from .liquidateSpotRecord import LiquidateSpotRecordJSON,LiquidateSpotRecord;
from . import liquidationMultiplierType
from .liquidationMultiplierType import LiquidationMultiplierTypeJSON,LiquidationMultiplierTypeKind;
from . import liquidationType
from .liquidationType import LiquidationTypeJSON,LiquidationTypeKind;
from . import lPAction
from .lPAction import LPActionJSON,LPActionKind;
from . import marginCalculationMode
from .marginCalculationMode import MarginCalculationModeJSON,MarginCalculationModeKind;
from . import marginMode
from .marginMode import MarginModeJSON,MarginModeKind;
from . import marginRequirementType
from .marginRequirementType import MarginRequirementTypeJSON,MarginRequirementTypeKind;
from . import marketIdentifier
from .marketIdentifier import MarketIdentifierJSON,MarketIdentifier;
from . import marketStatus
from .marketStatus import MarketStatusJSON,MarketStatusKind;
from . import marketType
from .marketType import MarketTypeJSON,MarketTypeKind;
from . import modifyOrderId
from .modifyOrderId import ModifyOrderIdJSON,ModifyOrderIdKind;
from . import modifyOrderParams
from .modifyOrderParams import ModifyOrderParamsJSON,ModifyOrderParams;
from . import modifyOrderPolicy
from .modifyOrderPolicy import ModifyOrderPolicyJSON,ModifyOrderPolicyKind;
from . import oracleGuardRails
from .oracleGuardRails import OracleGuardRailsJSON,OracleGuardRails;
from . import oracleSource
from .oracleSource import OracleSourceJSON,OracleSourceKind;
from . import oracleValidity
from .oracleValidity import OracleValidityJSON,OracleValidityKind;
from . import order
from .order import OrderJSON,Order;
from . import orderAction
from .orderAction import OrderActionJSON,OrderActionKind;
from . import orderActionExplanation
from .orderActionExplanation import OrderActionExplanationJSON,OrderActionExplanationKind;
from . import orderFillerRewardStructure
from .orderFillerRewardStructure import OrderFillerRewardStructureJSON,OrderFillerRewardStructure;
from . import orderParams
from .orderParams import OrderParamsJSON,OrderParams;
from . import orderStatus
from .orderStatus import OrderStatusJSON,OrderStatusKind;
from . import orderTriggerCondition
from .orderTriggerCondition import OrderTriggerConditionJSON,OrderTriggerConditionKind;
from . import orderType
from .orderType import OrderTypeJSON,OrderTypeKind;
from . import perpBankruptcyRecord
from .perpBankruptcyRecord import PerpBankruptcyRecordJSON,PerpBankruptcyRecord;
from . import perpFulfillmentMethod
from .perpFulfillmentMethod import PerpFulfillmentMethodJSON,PerpFulfillmentMethodKind;
from . import perpOperation
from .perpOperation import PerpOperationJSON,PerpOperationKind;
from . import perpPosition
from .perpPosition import PerpPositionJSON,PerpPosition;
from . import placeAndTakeOrderSuccessCondition
from .placeAndTakeOrderSuccessCondition import PlaceAndTakeOrderSuccessConditionJSON,PlaceAndTakeOrderSuccessConditionKind;
from . import poolBalance
from .poolBalance import PoolBalanceJSON,PoolBalance;
from . import positionDirection
from .positionDirection import PositionDirectionJSON,PositionDirectionKind;
from . import positionUpdateType
from .positionUpdateType import PositionUpdateTypeJSON,PositionUpdateTypeKind;
from . import postOnlyParam
from .postOnlyParam import PostOnlyParamJSON,PostOnlyParamKind;
from . import prelaunchOracleParams
from .prelaunchOracleParams import PrelaunchOracleParamsJSON,PrelaunchOracleParams;
from . import priceDivergenceGuardRails
from .priceDivergenceGuardRails import PriceDivergenceGuardRailsJSON,PriceDivergenceGuardRails;
from . import referrerStatus
from .referrerStatus import ReferrerStatusJSON,ReferrerStatusKind;
from . import rFQMakerMessage
from .rFQMakerMessage import RFQMakerMessageJSON,RFQMakerMessage;
from . import rFQMakerOrderParams
from .rFQMakerOrderParams import RFQMakerOrderParamsJSON,RFQMakerOrderParams;
from . import rFQMatch
from .rFQMatch import RFQMatchJSON,RFQMatch;
from . import rFQOrderId
from .rFQOrderId import RFQOrderIdJSON,RFQOrderId;
from . import settlePnlExplanation
from .settlePnlExplanation import SettlePnlExplanationJSON,SettlePnlExplanationKind;
from . import settlePnlMode
from .settlePnlMode import SettlePnlModeJSON,SettlePnlModeKind;
from . import signatureVerificationError
from .signatureVerificationError import SignatureVerificationErrorJSON,SignatureVerificationErrorKind;
from . import spotBalanceType
from .spotBalanceType import SpotBalanceTypeJSON,SpotBalanceTypeKind;
from . import spotBankruptcyRecord
from .spotBankruptcyRecord import SpotBankruptcyRecordJSON,SpotBankruptcyRecord;
from . import spotFulfillmentConfigStatus
from .spotFulfillmentConfigStatus import SpotFulfillmentConfigStatusJSON,SpotFulfillmentConfigStatusKind;
from . import spotFulfillmentMethod
from .spotFulfillmentMethod import SpotFulfillmentMethodJSON,SpotFulfillmentMethodKind;
from . import spotFulfillmentType
from .spotFulfillmentType import SpotFulfillmentTypeJSON,SpotFulfillmentTypeKind;
from . import spotOperation
from .spotOperation import SpotOperationJSON,SpotOperationKind;
from . import spotPosition
from .spotPosition import SpotPositionJSON,SpotPosition;
from . import stakeAction
from .stakeAction import StakeActionJSON,StakeActionKind;
from . import swapDirection
from .swapDirection import SwapDirectionJSON,SwapDirectionKind;
from . import swapReduceOnly
from .swapReduceOnly import SwapReduceOnlyJSON,SwapReduceOnlyKind;
from . import swiftOrderId
from .swiftOrderId import SwiftOrderIdJSON,SwiftOrderId;
from . import swiftOrderParamsMessage
from .swiftOrderParamsMessage import SwiftOrderParamsMessageJSON,SwiftOrderParamsMessage;
from . import swiftTriggerOrderParams
from .swiftTriggerOrderParams import SwiftTriggerOrderParamsJSON,SwiftTriggerOrderParams;
from . import swiftUserOrdersFixed
from .swiftUserOrdersFixed import SwiftUserOrdersFixedJSON,SwiftUserOrdersFixed;
from . import twapPeriod
from .twapPeriod import TwapPeriodJSON,TwapPeriodKind;
from . import userFees
from .userFees import UserFeesJSON,UserFees;
from . import userStatus
from .userStatus import UserStatusJSON,UserStatusKind;
from . import validityGuardRails
from .validityGuardRails import ValidityGuardRailsJSON,ValidityGuardRails;
