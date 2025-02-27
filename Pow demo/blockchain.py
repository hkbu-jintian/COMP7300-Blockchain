class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 5  # Set the difficulty level

    def create_genesis_block(self):
        # The first block in the blockchain (hardcoded)
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        mine_block(new_block, self.difficulty)  # Mine the block
        self.chain.append(new_block)

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Combine block data into a string and hash it
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

def mine_block(block, difficulty):
    target = "0" * difficulty  # e.g., "0000" for difficulty 4
    while block.hash[:difficulty] != target:
        block.nonce += 1  # Increment the nonce
        block.hash = block.calculate_hash()  # Recalculate the hash
    print(f"Block mined: {block.hash}")

import time
import hashlib

# Create the blockchain
blockchain = Blockchain()

# Add blocks to the blockchain
print("Mining block 1...")
blockchain.add_block(Block(1, "", time.time(), "Block 1 Data"))

print("Mining block 2...")
blockchain.add_block(Block(2, "", time.time(), "Block 2 Data"))

# Print the blockchain
for block in blockchain.chain:
    print(f"Block {block.index} [Hash: {block.hash}, Nonce: {block.nonce}]")
