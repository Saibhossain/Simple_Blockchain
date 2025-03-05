import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash, proof):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.proof = proof
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.proof}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0", 0)

    def get_last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    def valid_proof(self, last_proof, proof):
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Difficulty: 4 leading zeros

    def add_block(self, data):
        last_block = self.get_last_block()
        proof = self.proof_of_work(last_block.proof)
        new_block = Block(len(self.chain), time.time(), data, last_block.hash, proof)
        self.chain.append(new_block)

    def display_chain(self):
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Current Hash: {block.hash}")
            print(f"Proof: {block.proof}\n")
            print("-" * 40)

# Create blockchain and add blocks
my_blockchain = Blockchain()
my_blockchain.add_block("First Transaction")
my_blockchain.add_block("Second Transaction")

# Display the blockchain
my_blockchain.display_chain()
