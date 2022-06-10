import time


class Block:

    def __init__(self, transactions, lastHash, forger, blockCount):
        self.transactions = transactions
        self.lastHash = lastHash
        self.forger = forger
        self.blockCount = blockCount
        self.timestamp = time.time()
        self.signature = ''

    def toJson(self):
        data = {}
        jsonTransactions = []
        data['lastHash'] = self.lastHash
        data['forger'] = self.forger
        data['blockCount'] = self.blockCount
        data['timestamp'] = self.timestamp
        data['signature'] = self.signature
        # for transaction in self.transactions:
        #     jsonTransactions.append(transaction.toJson())
        # data['transactions'] = jsonTransactions
        # same thing as above
        data['transactions'] = [tx.toJson() for tx in self.transactions]
        return data
