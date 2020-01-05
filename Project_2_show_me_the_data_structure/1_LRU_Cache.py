from collections import OrderedDict
# https://github.com/python/cpython/blob/090bc148834aa4c92c683c2c07be572c31dd1b68/Lib/collections/__init__.py#L81


class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.num_element = 0
        self.cache_dict = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache_dict:
            # This is to make sure the use operation moves the item to the end of the cache_dict so that we can keep track of least recent used order
            self.cache_dict.move_to_end(key, last=True)
            return self.cache_dict[key]
        else:
            return -1

    def set(self, key, value):
        if self.capacity == 0:
            return
        # Set the value if there's spaceIf the cache is at capacity remove the oldest item.
        if self.is_full():
            self.remove_least_recently_used()
        else:
            # This is only needed when cache_dict is not full, because when it's full, we first delete the least recent, and add one again, num_element keeps the same
            self.num_element += 1
        self.cache_dict[key] = value

    def is_full(self):
        return self.num_element >= self.capacity

    def remove_least_recently_used(self):
        # last = False is needed because we want to pop the item in an FIFO way, by default last = True, then it will behave like a stack, LIFO
        self.cache_dict.popitem(last=False)

# Test 1
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))     # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))   # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print('test 2 \n')
# Test 2: When the size is 0, shouldn't be abel to set any values, and when getting values, should always output -1
our_cache = LRU_Cache(0)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))     # returns -1
print(our_cache.get(2))       # returns -1
print(our_cache.get(9))   # returns -1

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1

# Test 3: When setting the same key with a different value, the cache should be updated.
print('test 3 \n')
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(1, 10)
our_cache.set(4, 3)
our_cache.set(3, 3)
our_cache.set(4, 40)


print(our_cache.get(1))     # returns 10
print(our_cache.get(2))      # returns -1
print(our_cache.get(4))      # returns 40
print(our_cache.get(9))     # returns -1

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1