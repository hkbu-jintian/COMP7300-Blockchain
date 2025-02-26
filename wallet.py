from ecdsa import SigningKey, VerifyingKey, SECP256k1
import binascii
import os

class Wallet:
    def __init__(self, node_id):
        self.private_key = None
        self.public_key = None  # The public key is the address of each wallet
        self.node_id = node_id  # The port number

    # Save the public and private keys to variables
    def create_keys(self):
        private_kay, public_key = self.generate_keys()
        self.private_key = private_kay
        self.public_key = public_key
    
    # Save the public and private keys
    def save_keys(self):
        if self.public_key != None and self.private_key != None:
            try:
                # Create wallet directory if it doesn't exist
                os.makedirs('wallet', exist_ok=True)
                with open('wallet/wallet-{}.txt'.format(self.node_id), mode='w') as f:
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
            with open('wallet/wallet-{}.txt'.format(self.node_id), mode='r') as f:
                keys = f.readlines()
                public_key = keys[0][:-1]  # Because the public key was written with '\n', the last character is not read
                private_key = keys[1]
                self.public_key = public_key
                self.private_key = private_key
            return True
        except (IOError, IndexError):
            print('Loading wallet failed...')
            return False

    # Generate and return the public and private key pair using ECC
    def generate_keys(self):
        sk = SigningKey.generate(curve=SECP256k1)
        vk = sk.get_verifying_key()
        return (binascii.hexlify(sk.to_string()).decode('ascii'),
                binascii.hexlify(vk.to_string()).decode('ascii'))

    # Generate signature 
    # When signing, the DER encoding is converted to uncompressed encoding
    def sign_transaction(self, sender, recipient, amount):

        sk = SigningKey.from_string(binascii.unhexlify(self.private_key), curve=SECP256k1)
        h = (str(sender) + str(recipient) + str(amount)).encode('utf8')
        signature = sk.sign(h) # The generated signature is binary
        # The format of signature is DER encoding, which needs to be converted to uncompressed encoding
        return binascii.hexlify(signature).decode('ascii')

    # Verify signature
    @staticmethod
    def verify_transaction(transaction):
        vk = VerifyingKey.from_string(binascii.unhexlify(transaction.sender), curve=SECP256k1)
        h = (str(transaction.sender) + str(transaction.recipient) + str(transaction.amount)).encode('utf8')
        return vk.verify(binascii.unhexlify(transaction.signature), h)
        # verify always return True or False
