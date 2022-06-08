from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from BlockchainUtils import BlockchainUtils
from Transaction import Transaction


class Wallet:
    def __init__(self):
        self.keyPair = RSA.generate(2048)

    def sign(self, data):
        dataHash = BlockchainUtils.hash(data)
        signatureSchemeObject = PKCS1_v1_5.new(self.keyPair)
        signature = signatureSchemeObject.sign(dataHash)
        return signature.hex()

    @staticmethod
    def signatureValid(data, signature, publicKeyString):
        """
        :param data: the signature created on initially
        :param signature: to check if it's true/valid
        :param publicKeyString: the public key from the wallet RSA key pair
        :return: signatureValid: Boolean value
        """
        signature = bytes.fromhex(signature)
        dataHash = BlockchainUtils.hash(data)
        publicKey = RSA.importKey(publicKeyString)
        signatureSchemeObject = PKCS1_v1_5.new(publicKey)
        # checks if the signature corresponds to this data hash based on the public key
        signatureValid = signatureSchemeObject.verify(dataHash, signature)
        return signatureValid

    def publicKeyString(self):
        """
        This returns the public key from key pair, we are using exportKey('PEM') to get the binary data, then using
        decode to get the string data
        :return: publicKeyString: String
        """
        publicKeyString = self.keyPair.publickey().exportKey('PEM').decode('utf-8')
        return publicKeyString

    def createTransaction(self, receiver, amount, transType):
        transaction = Transaction(self.publicKeyString(), receiver, amount, transType)
        signature = self.sign(transaction.payload())
        transaction.sign(signature)
        return transaction

