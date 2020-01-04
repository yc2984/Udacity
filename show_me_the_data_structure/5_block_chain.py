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

        hash_str = self.data.encode('utf-8')  # In python 3, the encoded type is byte

        sha.update(hash_str)

        return sha.hexdigest()

"""Above is an example of attributes you could find in a Block class.

Finally you need to link all of this together in a block chain, which you will be doing by implementing it in a linked list. 
All of this will help you build up to a simple but full blockchain implementation!"""


class BlockChain:

    def __init__(self):
        self.head = None

    def size(self):
        block = self.head
        size = 0
        while block:
            block = block.next
            size += 1
        return size

    def append(self, timestamp, data):

        new_block = Block(timestamp, data)
        if not self.head:
            self.head = new_block
            return

        block = self.head
        while block.next:
            block = block.next
        new_block.previous_hash = block.hash
        block.next = new_block

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
my_block_chain.append(datetime(2020, 1, 2), 'This is the second block of my block chain')
my_block_chain.append(datetime(2020, 1, 3), 'This is the third block of my block chain')
my_block_chain.print()

empty_chain = BlockChain()
empty_chain.print()

