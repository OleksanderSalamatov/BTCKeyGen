import hashlib
import string
from math_utils import base58
from graphenebase import PrivateKey
from graphenebase.bip38 import encrypt

#STEP 1
seed = input(" Enter seed: ")

#STEP 2
hash = hashlib.sha256((seed).encode('utf8')).hexdigest()
print ("\n","Seed hash: ", hash, "\n")

#STEP 3
if int(hash, 16) < 2**256:
    print (" [SUCCESS] Hash is correct")
else:
    print (" [ERROR] Hash is not correct")
    quit()

#STEP 4
BTC_address = "80"+hash
print ("\n Formatted to BTC format key:", BTC_address)
BTC_compressed = BTC_address+"01"

#STEP 5
int_hex = int(BTC_address, 16)
int_bytes = int_hex.to_bytes(len(BTC_address)//2, 'big')
checksum1 = hashlib.sha256((int_bytes)).hexdigest()
int_hex = int(checksum1, 16)
int_bytes = int_hex.to_bytes(len(checksum1)//2, 'big')
checksum2 = hashlib.sha256((int_bytes)).hexdigest()
for i in range(8):
    BTC_address = BTC_address + checksum2[i]
print ("\n", "Private key: ", BTC_address)

#STEP 6
privkey_int = base58.encode(BTC_address)
print ("\n" " Base58 privkey: ", privkey_int)

#STEP 7
int_hex = int(BTC_compressed, 16)
int_bytes = int_hex.to_bytes(len(BTC_compressed)//2, 'big')
checksum1 = hashlib.sha256((int_bytes)).hexdigest()
int_hex = int(checksum1, 16)
int_bytes = int_hex.to_bytes(len(checksum1)//2, 'big')
checksum2 = hashlib.sha256((int_bytes)).hexdigest()
for i in range(8):
    BTC_compressed = BTC_compressed + checksum2[i]
privkey_int_c = base58.encode(BTC_compressed)
print (" \n Base58 compressed privkey: ", privkey_int_c)

#STEP 8
phrase = input(" \n Enter passphrase: ")
BIP38 = format(encrypt(PrivateKey(hash), phrase), "encwif")
print ("\n BIP38 key: ", BIP38)

#RESULT
print ("\n Base16: ", hash, 
       "\n WIF: ", privkey_int, 
       "\n cWIF: ", privkey_int_c, 
       "\n BIP38: ", BIP38)