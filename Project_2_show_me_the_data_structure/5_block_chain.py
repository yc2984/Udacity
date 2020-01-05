"""Blockchain
A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation."""

"""We can break the blockchain down into three main parts.

First is the information hash:"""

import hashlib
from datetime import datetime

"""We do this for the information we want to store in the block chain such as transaction time, data, and information like the previous chain.
The next main component is the block on the blockchain:"""


class Block:

    def __init__(self, timestamp, data, previous_hash=None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        time_and_data = str(self.timestamp) + self.data
        hash_str = time_and_data.encode('utf-8')  # In python 3, the encoded type is byte

        sha.update(hash_str)

        return sha.hexdigest()

"""Above is an example of attributes you could find in a Block class.

Finally you need to link all of this together in a block chain, which you will be doing by implementing it in a linked list. 
All of this will help you build up to a simple but full blockchain implementation!"""


class BlockChain:

    def __init__(self):
        self.head = None
        self.tail = None

    def size(self):
        block = self.head
        size = 0
        while block:
            block = block.next
            size += 1
        return size

    def append(self, timestamp=None, data=None):
        if not timestamp or not data:
            print("empty data")
            return
        new_block = Block(timestamp, data)
        if not self.head:
            self.head = new_block
            self.tail = self.head
            return

        new_block.previous_hash = self.tail.hash
        self.tail.next = new_block
        self.tail = new_block

    def print(self):
        block = self.head
        index = 1
        print("there are in total {} blocks in this chain".format(self.size()))
        print('\n')
        while block:
            print("this is the {} th block of the chain".format(index))
            print('timestamp of this block: {}'.format(block.timestamp))
            print('data of this block: {}'.format(block.data))
            print('previous hash of this block: {}'.format(block.previous_hash))
            print('hash of this block: {}'.format(block.hash))
            print('\n')
            index += 1
            block = block.next


my_block_chain = BlockChain()
my_block_chain.append(datetime(2020, 1, 1), 'This is the first block of my block chain')
# this is the 1 th block of the chain
# timestamp of this block: 2020-01-01 00:00:00
# data of this block: This is the first block of my block chain
# previous hash of this block: None
# hash of this block: 7f517d63c85b338fc39dba5e7b71323331f289d5b7699bba623363263339feee
my_block_chain.append(datetime(2020, 1, 2), 'This is the second block of my block chain')
# this is the 2 th block of the chain
# timestamp of this block: 2020-01-02 00:00:00
# data of this block: This is the second block of my block chain
# previous hash of this block: 7f517d63c85b338fc39dba5e7b71323331f289d5b7699bba623363263339feee
# hash of this block: 754589f7a5bb789811739235a3b28c18a9ca53aba207569008d3488d740139d9
my_block_chain.append(datetime(2020, 1, 3), 'This is the third block of my block chain')
my_block_chain.print()
# this is the 3 th block of the chain
# timestamp of this block: 2020-01-03 00:00:00
# data of this block: This is the third block of my block chain
# previous hash of this block: 754589f7a5bb789811739235a3b28c18a9ca53aba207569008d3488d740139d9
# hash of this block: f8de026e0072b4eb6dce6b9c331ada0ded8283bcb0dc3a762941cb4c49ed81de

# Test: add None data
non_block_chain = BlockChain()
non_block_chain.append(datetime(2020, 1, 3), None)
non_block_chain.print()

# Test: add empty block
wrong_case = BlockChain()
wrong_case.append()
wrong_case.print()

