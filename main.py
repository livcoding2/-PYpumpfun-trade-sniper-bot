import requests
import time
import os
from pump_fun import buy, sell
import time
from colored import Fore, Back, Style
from solders.pubkey import Pubkey
from threading import Thread
from config import BUY_AMOUNT, SELL_TIMEOUT, CHECK_WEBSITE, CHECK_TELEGRAM, CHECK_TWITTER, client, PUB_KEY
bought_tokens = []

def get_new_tokens():
    endpoint_new_tokens = "https://client-api-2-74b1891ee9f9.herokuapp.com/coins?offset=0&limit=20&sort=created_timestamp&order=DESC&includeNsfw=true"
    endpoint_trades = "https://client-api-2-74b1891ee9f9.herokuapp.com/trades/%mint%?limit=20&offset=0"
    
    r = requests.get(url=endpoint_new_tokens)
    data = r.json()
    try:
        for coin in data:
            timestamp = coin["created_timestamp"]
            new_token = coin["mint"]
            website = coin["website"]
            telegram = coin["telegram"]
            twitter = coin["twitter"]
            
            if CHECK_WEBSITE == True and website == None:
                continue
            if CHECK_TELEGRAM == True and telegram == None:
                continue
            if CHECK_TWITTER == True and twitter == None:
                continue

            curr_timestamp = round(time.time() * 1000)
            if curr_timestamp - timestamp <= 8 * 1000:
                return new_token
        
        return ""
    except:
        print("Error getting new tokens!")
        return ""


os.system("cls")
print(f"\t{Fore.white}{Back.green} --- Pump.fun Sniper Bot ---\n")
print(f"{Style.reset}[-] Looking for tokens...")
while True:
    time.sleep(1)
    token = get_new_tokens()
    if token not in bought_tokens and token != "":
        bought_tokens.append(token)
        print(f"{Style.reset}\n[-] Attempting to buy ", token)
        sol_balance = client.get_balance(Pubkey.from_string(PUB_KEY), commitment="processed")
        confirm = buy(token, BUY_AMOUNT)
        if confirm == True:
            sentSell = False
            sellCounter = 0
            while sentSell == False:
                if sellCounter >= SELL_TIMEOUT:
                    print(f"{Fore.yellow}[-] Sending Sell TX ", token)
                    sentSell = sell(str(token))
                    if sentSell == True:
                        curr_balance = client.get_balance(Pubkey.from_string(PUB_KEY), commitment="processed")
                        print(f"{Fore.green}[!] Succesfully sold ", token, "\n\tProfit: " + str((float(curr_balance.value) - float(sol_balance.value)) / 1000000000), " SOL")
                else:
                    time.sleep(1)
                    sellCounter += 1
    time.sleep(0)

