from Crypto.PublicKey import RSA  # pycrypto 包
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import Crypto.Random
import binascii

class Wallet:
    def __init__(self, node_id):
        self.private_key = None
        self.public_key = None  # The public key is the address of each wallet
        self.node_id = node_id

    # Save the public and private keys to variables
    def create_keys(self):
        private_kay, public_key = self.generate_keys()
        self.private_key = private_kay
        self.public_key = public_key
    
    # Save the public and private keys
    def save_keys(self):
        if self.public_key != None and self.private_key != None:
            try:
                with open('/wallet/wallet-{}.txt'.format(self.node_id), mode='w') as f:
                    f.write(self.public_key)
                    f.write('\n')
                    f.write(self.private_key)
                return True
            except (IOError, IndexError):
                print('Saving wallet failed...')
                return False

    # Load the public and private keys from the local file
    def load_keys(self):
        try:
            with open('/wallet/wallet-{}.txt'.format(self.node_id), mode='r') as f:
                keys = f.readlines()
                public_key = keys[0][:-1]  # 因为写公钥的时候加了'\n'，所以最后一位不读
                private_key = keys[1]
                self.public_key = public_key
                self.private_key = private_key
            return True
        except (IOError, IndexError):
            print('Loading wallet failed...')
            return False

    # Generate and return the public and private key pair using RSA
    def generate_keys(self):
        private_key = RSA.generate(1024, Crypto.Random.new().read)
        public_key = private_key.publickey()
        return (
                binascii
                .hexlify(private_key.exportKey(format='DER'))
                .decode('ascii'),
                binascii
                .hexlify(public_key.exportKey(format='DER'))
                .decode('ascii')
            )
    
    # Generate signature
    def sign_transaction(self, sender, recipient, amount):
        signer = PKCS1_v1_5.new(RSA.importKey(binascii.unhexlify(self.private_key))) # type: ignore
        h = SHA256.new((str(sender) + str(recipient) + str(amount)).encode('utf8'))
        signature = signer.sign(h) # The generated signature is binary
        return binascii.hexlify(signature).decode('ascii') # Convert to hexadecimal using hexlify, and use ascii encoding

    # Verify signature
    @staticmethod
    def verify_transaction(transaction):
        # if transaction.sender == 'MINING':
        #     return True
        public_key = RSA.importKey(binascii.unhexlify(transaction.sender))
        verifier = PKCS1_v1_5.new(public_key)
        h = SHA256.new((str(transaction.sender) + str(transaction.recipient) + str(transaction.amount)).encode('utf8'))
        return verifier.verify(h, binascii.unhexlify(transaction.signature))
