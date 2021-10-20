import hashlib
import string
import base58
from math_utils.transform import toBinary
from math_utils import base58

#STEP 1
seed = input(" Enter seed: ")

#STEP 2
hash = hashlib.sha256((toBinary(seed)).encode('utf-8')).hexdigest()
print ("\n","Seed hash: ", hash, "\n")
hash_int = hex(int(hash, 16))

#STEP 3
if int(hash_int, 16) < 2**256:
    print (" [SUCCESS] Hash is correct")
else:
    print (" [ERROR] Hash is not correct")
    quit()

#STEP 4
BTC_address = "80"+hash
print ("\n Formatted to BTC format key:", BTC_address)

#STEP 5
checksum1 = hashlib.sha256((toBinary(BTC_address)).encode('utf-8')).hexdigest()
checksum2 = hashlib.sha256((toBinary(checksum1)).encode('utf-8')).hexdigest()
checksum2
for i in range(8):
    BTC_address = BTC_address + checksum2[i]
print ("\n", "Private key: ", BTC_address)

#STEP 6
privkey_int =  base58.encode(BTC_address)
print ("\n" " Base58 privkey: ", privkey_int)
