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
 
3. In <b>Wallet</b> class create a static method name ```signatureValid``` with three parameters named ```data, signature, publicKeyString```
<b>data</b> is the signature created on initially, <b>signature</b> to check if its true, <b>publicKeyString</b> is basically 
the public key from the wallet RSA key pair(this was used to sign the data)[we need it in string format]. Create a method
```publicKeyString``` which will return the public key extracted from ```self.keyPair``` as a string.
 
4. In <b>Transaction</b> class create a method ```payload```. We need a consistent representation, so for that we are
creating this function. In here we create a deep copy, so we are using ```copy``` library. in <b>Wallet</b> class create a method name 
```createTransaction```, what we have to provide is basically same which is in init method in <b>Transaction</b> apart from
sending a public key. Use the ```transaction.payload()``` to create the signature then sign it with it and then return the 
```transaction```. So now we can create sign transaction with one call. In the ```Main.py``` file test are we are testing if
a fraud wallet public key will work or not.

5. Create a new file name ```Transaction Pool```. So here we want ot create some kind of list which which is the transaction pool
which adds new transactions but make sure same transaction will not be added twice. Create a method ```addTransaction```
which will add new transaction, but we have to make sure that the same transaction must not exists twice, so we will create
another method ```transactionExists```. There are many ways to compare two transaction, we can use the uuid field
```self.id = uuid.uuid1().hex``` in <b>Transaction</b>  class which we have declared previously. To do that we are writing
a method in <b>Transaction</b> class named ```equals``` which will compare two ids of a transaction. Now we can call it
in ```transactionExists``` to check and verify.
