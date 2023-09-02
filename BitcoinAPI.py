import requests
import json


#to call an API wpython3 -m pip install requestse need to first specify an url
#some APIs require a key, here, we do not. The limit is 1000 calls per day.
#the documentation can be found at: #https://blockchair.com/api/docs#link_M2

# we call the information using a requests.get. 

url="https://api.blockchair.com/bitcoin/dashboards/block/0"
r=requests.get(url)
print(r) # A message 200 means success. 404 is not found.Take the habit of printing the initial response to see if it was succesful
r1=r.json() #converting the response to json file.
print(r1) #printing the file. You should see a bunch of numbers and text.
#if the response is not 200, then Python will give you an error.

#For this API, depending on the type of data you want, the URL will change
#see the manual for more details
#for other api, you use the same url but change the query parameters


########################################
#to get the info on the bitcoin network
########################################
url="https://api.blockchair.com/cardano/stats"
r=requests.get(url)
r1=r.json()
print(r1)
#to get the number of blocks mined
blocks=r1['data']['blocks']
print("The number of blocks in the BTC is "+str(blocks))

#to get the number of transactions in the last 24 hours
transactions=r1['data']['transactions_24h']
print("The number of transactions in the last 24 h in the BTC is "+str(transactions))

# to get hash of the last block mined
best_block_hash=r1['data']['best_block_hash']
print("The hash of the last block in the BTC is "+str(best_block_hash))


#to get the number of hashes computed in the past 24 hours:
hashes24=r1['data']['hashrate_24h'] 
print("The number of hashes computed in the last 24 hrs is "+str(best_block_hash))

#to get the median tx fee in the past 24 hours:
fee24h=r1['data']['median_transaction_fee_usd_24h'] 
print("The median fee in USD in the last 24 hrs is "+str(fee24h))

#to get BTC market share:
share=r1['data']['market_dominance_percentage']
print("The current BTC market share is: "+str(share)+"%")

#to get BTC total value:
valuedUSD=r1['data']['market_cap_usd'] 
valuedbillion=int(r1['data']['market_cap_usd']/10**9)
print("The current BTC market cap is: "+str(valuedbillion)+" billion")

'''
########################################
#to get block specific information on Bitcoin
########################################
block="760000"
url="https://api.blockchair.com/bitcoin/dashboards/block/"+str(block)
r=requests.get(url)
print(r) # A message 200 means success. 404 is not found.Take the habit of printing the initial response to see if it was succesful
r1=r.json() #converting the response to json file.

# to get the number of transactions in a block
num_tx=r1['data'][str(block)]['block']['transaction_count']
print("the number of transactions in block "+str(block)+ " is " +str(num_tx))

# to get the USD reward in a block
reward=r1['data'][str(block)]['block']['reward_usd']
print("The coinbase reward in block "+str(block)+ " is " +str(reward))

# to get the guessed miner in a block
miner=r1['data'][str(block)]['block']['guessed_miner']
print("The guessed miner in block "+str(block)+ " is " +str(miner))


# to get the merkle root in a block
hash1=r1['data'][str(block)]['block']['merkle_root']
print("The merkle root hash in the block is : "+str(hash1))

#to get the hashes of the transactions to get the root hash:
hash1=r1['data'][str(block)]['transactions']
print(hash1) #it is a long list!!!



#################################################
#to get the information on a transaction
#################################################
block="700000"
url="https://api.blockchair.com/bitcoin/dashboards/block/"+str(block)
r=requests.get(url)
print(r) # A message 200 means success. 404 is not found.Take the habit of printing the initial response to see if it was succesful
r1=r.json() #converting the response to json file.

#to get the hashes of the transactions to get the root hash:
print('Here is where we look at hash')
hash1=r1['data'][str(block)]['transactions'][0] #this is picking the hash of the 2nd tx#
print(hash1) #this is the hash of the tx we want to get#

url="https://api.blockchair.com/bitcoin/raw/transaction/"+str(hash1) 
r=requests.get(url)
print(r) # A message 200 means success. 404 is not found.Take the habit of printing the initial response to see if it was succesful
r1=r.json()
print(r1['data'][str(hash1)]['decoded_raw_transaction']) #this is the tx info#
print('this is input info')
# print(r1['data'][str(hash1)]['decoded_raw_transaction']['vin'][0]['vout']) #info of the inputs
for item in r1['data'][str(hash1)]['decoded_raw_transaction']['vout']:
    print(item['scriptPubKey']) #info of the outputs

'''