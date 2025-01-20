import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.current_hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        encoded_block = block_string.encode()
        return hashlib.sha256(encoded_block).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_first_block()]

    def create_first_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")

    def get_last_block(self):
        return self.chain[-1]

    def calculate_block_hash(self, index, timestamp, data, previous_hash):
            block_string = f"{index}{timestamp}{data}{previous_hash}"
            encoded_block = block_string.encode()
            return hashlib.sha256(encoded_block).hexdigest()

    def append_block(self, data):
        previous_block = self.get_last_block()
        new_index = previous_block.index + 1
        new_timestamp = datetime.datetime.now()
        new_previous_hash = previous_block.current_hash
        new_block = Block(new_index, new_timestamp, data, new_previous_hash)
        self.chain.append(new_block)
        return new_block

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.previous_hash != previous_block.current_hash:
                print(f"Error: Previous hash mismatch at block {current_block.index}")
                return False
            recalculated_hash = current_block.compute_hash()
            if current_block.current_hash != recalculated_hash:
                print(f"Error: Current hash invalid at block {current_block.index}")
                return False
        return True


# Example Usage (Modified for new method names)
if __name__ == "__main__":
    my_blockchain = Blockchain()

    print("Adding blocks...")
    my_blockchain.append_block("Transaction Data 1")
    my_blockchain.append_block("Salamat Transaction Data 2")
    my_blockchain.append_block("Another important transaction from Momodu")

    print("\nBlockchain contents:")
    for block in my_blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Current Hash: {block.current_hash}")
        print("-" * 30)

    print("\nVerifying blockchain integrity...")
    if my_blockchain.validate_chain():
        print("Blockchain is valid.")
    else:
        print("Blockchain is invalid.")

    print("\nTampering with the second block's data...")
    my_blockchain.chain[1].data = "MODIFIED DATA!"
    if my_blockchain.validate_chain():
        print("Blockchain is valid.")
    else:
        print("Blockchain is invalid.")