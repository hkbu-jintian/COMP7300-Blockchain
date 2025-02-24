from collections import OrderedDict
from utility.printable import Printable

class Transaction(Printable):
    """A transaction which can be added to a block in the blockchain
    
    Attributes:
        :sender: The sender of the coins
        :recipient: The recipient of the coins
        :signature: The signature of the transaction
        :amount: The amount of coins sent
    """
    def __init__(self, txid, sender, recipient, signature, amount):
        self.txid = txid
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature
    
    def to_ordered_dict(self):
        # Use the python built-in OrderedDict library to create a sorted dictionary
        # This can avoid the problem of verification failure due to the order of the string
        return OrderedDict([
            ('sender', self.sender),
            ('recipient', self.recipient),
            ('amount', self.amount)
        ])