# Python-Blockchain
Step by step guide if anyone wants to build it in any other language

1. Create a class name <b>Transaction</b> and add ```senderPublicKey, receiverPublicKey, amount, transType``` variables to be 
initialize at the very beginning. Three other variables to be initialize in the constructor ```timestamp, id, signature```, 
id can be uuid1, timestamp is pretty self explanatory, and signature will be added later for now it's an empty string.
```toJson()``` method is for printing a proper data. can also be achieved by doing ```print(transaction.__dict__)``` instead of 
```print(transaction.toJson())```

2. Create a <b>Wallet</b> class, I am using Crypto package (RSA) for key pair. Initialize a```keyPair``` variable in the constructor.
Create a <b>sign method</b> which in takes some data and generate a key pair. Create a <b>BlockchainUtils</b> class, implement a 
hash method, in here I am using ```json.dumps(data)``` to return a string. then converting it a byte representation, because we
are using ```Crypto.Hash import SHA256``` here to hash. From ```Crypto.Signature import PKCS1_v1_5``` to generate signature and
also to validate signatures. In the ```sign()``` function we are generating a signature from the data hash. Whiting a ```sign()```
 function in <b>Transaction</b> class which will set the signature in <b>Transaction</b> class.