from Transaction import Transaction
from Wallet import Wallet

if __name__ == '__main__':
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    transType = 'TRANSFER'

    transaction = Transaction(sender, receiver, amount, transType)

    wallet = Wallet()
    signature = wallet.sign(transaction.toJson())
    print(signature)
    transaction.sign(signature)
    print(transaction.toJson())
