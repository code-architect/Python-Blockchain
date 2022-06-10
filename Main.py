from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from pprint import pprint

if __name__ == '__main__':
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    transType = 'TRANSFER'

    # transaction = Transaction(sender, receiver, amount, transType)
    #
    # wallet = Wallet()
    # signature = wallet.sign(transaction.toJson())
    # # print(signature)
    #
    # transaction.sign(signature)
    # print(transaction.toJson())
    # print("-----------------------------------------------------------------------------------------")
    # print(signature)
    # print("-----------------------------------------------------------------------------------------")
    # print(wallet.publicKeyString())
    # print("-----------------------------------------------------------------------------------------")
    # signatureValid = Wallet.signatureValid(transaction.payload(), signature, wallet.publicKeyString())
    # print(signatureValid)

    # wallet = Wallet()
    # transaction = wallet.createTransaction(receiver, amount, transType)
    # pprint(transaction.toJson())
    # print("-----------------------------------------------------------------------------------------")
    # signatureValid = Wallet.signatureValid(transaction.payload(), transaction.signature, wallet.publicKeyString())
    # print("-----------------------------------------------------------------------------------------")
    # pprint(transaction.signature)
    # print("-----------------------------------------------------------------------------------------")
    # pprint(wallet.publicKeyString())
    # print("-----------------------------------------------------------------------------------------")
    # pprint(signatureValid)

    # wallet = Wallet()
    # fraudelentWallet = Wallet()
    # transaction = wallet.createTransaction(receiver, amount, transType)
    # signatureValid = Wallet.signatureValid(transaction.payload(), transaction.signature, fraudelentWallet.publicKeyString())
    # pprint(signatureValid)

    wallet = Wallet()
    fraudelentWallet = Wallet()
    pool = TransactionPool()
    transaction = wallet.createTransaction(receiver, amount, transType)

    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)

    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)

    pprint(pool.transactions)
