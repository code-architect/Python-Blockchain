# Python-Blockchain
Step by step guide if anyone wants to build it in any other language

1. Create a class name Transaction and add ```senderPublicKey, receiverPublicKey, amount, transType``` variables to be 
initialize at the very beginning. Three other variables to be initialize in the constructor ```timestamp, id, signature```, 
id can be uuid1, timestamp is pretty self explanatory, and signature will be added later for now it's an empty string.
```toJson()``` method is for printing a proper data. can also be achieved by doing ```print(transaction.__dict__)``` instead of 
```print(transaction.toJson())```

