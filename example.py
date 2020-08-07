import satoshi

# Example of json returned via Bitmex REST API '/wallet/' endpoint 
bitmex_balance = {
    "account": 10001,
    "currency": "XBt",
    "prevDeposited": 63750000,
    "prevWithdrawn": 82315823,
    "prevTransferIn": 0,
    "prevTransferOut": 0,
    "prevAmount": 141022792,
    "prevTimestamp": "2020-08-06T12:00:00.000Z",
    "deltaDeposited": 0,
    "deltaWithdrawn": 0,
    "deltaTransferIn": 0,
    "deltaTransferOut": 0,
    "deltaAmount": 0,
    "deposited": 63750000,
    "withdrawn": 82315823,
    "transferIn": 0,
    "transferOut": 0,
    "amount": 141022792,
    "pendingCredit": 0,
    "pendingDebit": 0,
    "confirmedDebit": 0,
    "timestamp": "2020-08-06T12:00:02.710Z",
    "addr": "-",
    "script": "-",
    "withdrawalLock": []
}

if __name__ == "__main__":
    # Opening
    print("\n\nWelcome to > satoshi \n")
    satoshi.print_art()
    print("\n\nOld Balance Object: \n")
    print(bitmex_balance)

    # Usage
    satoshis = bitmex_balance.get('amount')
    usd = satoshi.to_fiat(satoshis)
    bitmex_balance['usdValue'] = usd
    brl = satoshi.to_fiat(satoshis, 'BRL')
    bitmex_balance['brlValue'] = brl

    # Result
    print("\n\nNew Balance Object: \n")
    print(bitmex_balance)