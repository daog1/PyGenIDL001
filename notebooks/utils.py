from solana.rpc.api import Client
from solana.rpc.types import TxOpts
import json
from solders.signature import Signature
from solders.pubkey import Pubkey
import os

def find_program_index(tx,program_id):
    message = tx.value.transaction.transaction.message
    account_keys = message.account_keys
    for i, account in enumerate(account_keys):
        if account == program_id:
            return i
    return -1

def getTx(rpc,txHash):
    client = Client(os.getenv(rpc))
    tx = client.get_transaction( Signature.from_string(txHash), encoding="json", max_supported_transaction_version=0)
    return tx