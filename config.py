from solana.rpc.api import Client
from solders.keypair import Keypair
import os
from time import sleep

PUB_KEY = ""
PRIV_KEY = ""
BUY_AMOUNT = 0.01
SELL_TIMEOUT = 30
CHECK_TELEGRAM = True
CHECK_WEBSITE = False
CHECK_TWITTER = False

RPC = ""

if PUB_KEY == "" or PRIV_KEY == "" or RPC == "":
    print("[x] Invalid or missing settings.\n    Open 'config.py' and fill the required fields.")
    os._exit(0)
else:
    client = Client(RPC)
    payer_keypair = Keypair.from_base58_string(PRIV_KEY)
