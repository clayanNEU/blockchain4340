import ecdsa
import hashlib
from ecdsa.util import randrange_from_seed__trytryagain as seedkey
import random
import time
import base58
import base58check
import codecs



def keys():
    seed=input('Select a seed, must be an integer: ')
    secret_exp=seedkey(seed,ecdsa.SECP256k1.order)
    privkey1=ecdsa.SigningKey.from_secret_exponent(secret_exp, curve=ecdsa.SECP256k1)
    pubkey1=privkey1.get_verifying_key()
    print("The private key is :"+privkey1.to_string().hex())
    print("The public key is :"+pubkey1.to_string().hex())



def bitcoin_add():
    pubkey1=str(input('Type the public key:'))
    if pubkey1[0:1]=='0':
        temp1=pubkey1
    else:
        temp1="04"+pubkey1
    print('Step a) is :'+temp1)
    temp1b=bytes.fromhex(temp1)
    #b
    temp2=hashlib.sha256(temp1b)
    temp3b=temp2.digest()
    temp3hex=temp2.hexdigest()
    print('Step b) is :'+temp3hex)
    print('Step b) in bytes is :'+str(temp3b))
    ##this is to compute the RIPEMD160...40 char long in hex
    temp4=hashlib.new('ripemd160')
    temp4.update(temp3b) ####check! temp4.update(temp3hex.encode())
    temp5b=temp4.digest()
    temp5hex=temp4.hexdigest()
    print('Step c) is :'+temp5hex)
    ##adding the 00
    temp6hex="00"+temp5hex
    print('Step d) is :'+temp6hex)
    temp6b=bytes.fromhex(temp6hex)
    ##computing the hash again using sha256
    temp7=hashlib.sha256(temp6b)
    temp8hex=temp7.hexdigest()
    print('Step e) is :'+temp8hex)
    temp8b=temp7.digest()
    ##compute the hash again
    temp9=hashlib.sha256(temp8b)
    temp10hex=temp9.hexdigest()
    print('Step f) is :'+temp10hex)
    temp10b=temp9.digest()
    ##taking the first 4 bytes (the checksum)
    checksum=temp10hex[0:8]
    print('Step g) is :'+checksum)
    ##take d) and concatenate the checksum
    temp11hex=temp6hex+checksum
    print('Step h) is :'+temp11hex)
    temp11b=bytes.fromhex(temp11hex)
    ##convert to base 58
    temp13=base58check.b58encode(temp11b)
    temp14=str(temp13)
    print('Step i) is :'+temp14)
bitcoin_add()
    
def op_hash160():
    pubkey1=str(input('Type the public key:'))
    temp1="04"+pubkey1
    temp1b=bytes.fromhex(temp1)
    #b
    temp2=hashlib.sha256(temp1b)
    temp3b=temp2.digest()
    temp3hex=temp2.hexdigest()
    ##this is to compute the RIPEMD160...40 char long in hex
    temp4=hashlib.new('ripemd160')
    temp4.update(temp3b) ####check! temp4.update(temp3hex.encode())
    temp5b=temp4.digest()
    temp5hex=temp4.hexdigest()
    print('The OP_HASH160 is :'+temp5hex)    

def signature():
    seed=input('Select a seed, must be an integer: ')
    secret_exp=seedkey(seed,ecdsa.SECP256k1.order)
    privkey1=ecdsa.SigningKey.from_secret_exponent(secret_exp, curve=ecdsa.SECP256k1)
    pubkey1=privkey1.get_verifying_key()
    temp1=input('Type the message. If this is BTC, type the hash of transaction that you will use:')
    temp2=bytes.fromhex(temp1)
    thesignature1=privkey1.sign(temp2,hashfunc=hashlib.sha256)
    pubkey1=privkey1.get_verifying_key()
    print("The public key is :"+pubkey1.to_string().hex())
    print("The signature is: "+thesignature1.hex( ))


def header():
    version=str(input('Type the version of the client: '))
    prevhash=input('Type the hash of the previous block: ')
    root=input('Type the root of the merkle tree: ')
    timestamp=str(input('Type date in Unix format: '))
    diff=str(input('Type the level of difficulty, the bits: '))
    nonce1=str(input('What is the nonce?: '))
    temp1=version+prevhash+root+timestamp+diff+nonce1
    if len(temp1)*0.5==int(len(temp1)*0.5):
        padding='000000000000'
    else:
        padding='0000000000000'
    headerall=version+prevhash+root+timestamp+diff+nonce1+padding
    headerprint='The respective header is:'+"\n"+headerall
    print(headerprint)
    return headerall

def header_sha256():
    header=input('What is the header?: ')
    temp1b=bytes.fromhex(header)
    temp2=hashlib.sha256(temp1b)
    temp3b=temp2.digest()
    temp3hex=temp2.hexdigest()
    return temp3hex
    print('The hash of the header is :'+temp3hex)



#see v_3 for details on the solutions


def pow_print():
    target=str(input('What is the target hash? :'))
    version=input('Type the version of the client: ')
    prevhash=input('Type he hash of the previous block: ')
    root=input('Type the root of the merkle tree: ')
    timestamp=input('Type date in Unix format: ')
    diff=input('Type the level of difficulty, the bits: ')

    notvalid=[741395282,662299907]
    nattempts=0
    while True:
        nattempts+=1
        nonce1=str(int(random.randrange(0,100000000,1)))
        temp1=version+prevhash+root+timestamp+diff+nonce1
        if len(temp1)*0.5==int(len(temp1)*0.5):
            padding='000000000000'
        else:
            padding='0000000000000'
        headerall=version+prevhash+root+timestamp+diff+nonce1+padding
        temp1b=bytes.fromhex(headerall)
        temp2=hashlib.sha256(temp1b)
        temp3hex=temp2.hexdigest()
        if temp3hex<target and (nonce1 not in notvalid):
            print('The Nonce is :'+nonce1)
            print('The hash is '+temp3hex)
            break
        if nattempts>10**9:
            print('I tried '+str(nattempts)+' combinations')
            break


def pow_print2():
#    target=str(input('What is the target hash? :'))
#    version=input('Type the version of the client: ')
#    prevhash=input('Type he hash of the previous block: ')
#    root=input('Type the root of the merkle tree: ')
#    timestamp=input('Type date in Unix format: ')
#    diff=input('Type the level of difficulty, the bits: ')

    target='0'*6+'0e70e7'+'0'*52
    version='1'
    prevhash='0000000429383d492e95c9d3ce82e5f4ea9ddd5b10aba18390064aee3aa743a5'
    root='c32f14af9c395212488c2d507992e3dddbabcfdc240b0929d3d5ca13c1a6a74e'
    timestamp='1646328541'
    diff='487475671'

    
    for j in range(10**9):
        nonce1=str(j)
        temp1=version+prevhash+root+timestamp+diff+nonce1
        if len(temp1)*0.5==int(len(temp1)*0.5):
            padding='000000000000'
        else:
            padding='0000000000000'
        headerall=version+prevhash+root+timestamp+diff+nonce1+padding
        temp1b=bytes.fromhex(headerall)
        temp2=hashlib.sha256(temp1b)
        temp3hex=temp2.hexdigest()
        if temp3hex<target:
            print('The Nonce is :'+nonce1)
            print('The hash is '+temp3hex)
            break    
        

#pow_print2()

def op_hash160_v2():
    pubkey1=str(input('Type the public key:'))
    temp1b=bytes.fromhex(pubkey1)
    temp2=hashlib.sha256(temp1b)
    temp3b=temp2.digest()
    temp3hex=temp2.hexdigest()
    temp4=hashlib.new('ripemd160')
    temp4.update(temp3b) ####check! temp4.update(temp3hex.encode())
    temp5b=temp4.digest()
    temp5hex=temp4.hexdigest()
    print('The OP_HASH160 is :'+temp5hex)    

op_hash160_v2()