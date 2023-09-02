import hashlib


# sha 256
themessage = "Hello"

# byte format
newmessage = themessage.encode()
print(newmessage)

hash1 = hashlib.sha256(newmessage)
print(hash1)

formatted_hash = hash1.hexdigest()
print("The hash of ("+themessage+") is : "+formatted_hash)


# Linked Lists
import json

class myfirstchain:
    id = None
    text = None
    parent_id = None

block1 = myfirstchain()
block1.id = 1259 
block1.parent_id = "None"
block1.text = "Tx 234"

print(block1.__dict__)



# Linked list Hash
class myfirstchainwithhash:
    def __init__(self, blockid, blocktext, parentid, prevblockhash):
        self.id = str(blockid)
        self.text = str(blocktext)
        self.parent_id = (parentid)
        self.prevhash = hashlib.sha256(json.dumps(prevblockhash).encode('utf-8')).hexdigest()


# merkle trees
