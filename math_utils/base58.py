import string

def encode(BTC):
    base58check = ''
    BTC_int = int(BTC, 16)
    alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    while (1):
        base58check = alphabet[(BTC_int % 58)] + base58check
        BTC_int = BTC_int//58
        if BTC_int <= 1:
            break
    return (base58check)