from Transaction import Transaction

if __name__ == '__main__':
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    transType = 'TRANSFER'

    transaction = Transaction(sender, receiver, amount, transType)
    print(transaction.toJson())
