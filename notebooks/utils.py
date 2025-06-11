from solana.rpc.api import Client
from solana.rpc.types import TxOpts
import json
from solders.signature import Signature
from solders.pubkey import Pubkey
import os
import based58

def find_program_index(tx,program_id):
    message = tx.value.transaction.transaction.message
    if isinstance(program_id,str):
        program_id = Pubkey.from_string(program_id)
    account_keys = message.account_keys
    for i, account in enumerate(account_keys):
        if account == program_id:
            return i
    return -1

def getTx(rpc,txHash):
    client = Client(os.getenv(rpc))
    if isinstance(txHash,Signature):
        tx = client.get_transaction(txHash, encoding="json", max_supported_transaction_version=0)
    else:
        tx = client.get_transaction(Signature.from_string(txHash), encoding="json", max_supported_transaction_version=0)
    return tx


def PrintTxByProgramId(programId, tx):
    for i, instruction in enumerate(tx.value.transaction.transaction.message.instructions):
        if instruction.program_id_index == programId:
            bindata = based58.b58decode(instruction.data.encode('utf-8')) #//[:8]
            print(f"{tx.value.transaction.transaction.signatures[0]} ix {i}: {bindata.hex()}")