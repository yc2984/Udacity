We need to find a data structure that can maintain the sequence of the elements (cache items) and can easily adjust the sequence when an operation use happens. 
The reason to choose OrderedDict is that it fulfils both of the requirement. The get, move_to_end and popitem method all takes constant time. The implementation can be found here: https://github.com/python/cpython/blob/090bc148834aa4c92c683c2c07be572c31dd1b68/Lib/collections/__init__.py#L81

**get method**
The time complexity of get method is O(1). 
    - To check if a key exists in an OrderedDict takes O(1).
    - move_to_end method also takes O(1). 
    - get an element by key from an OrderedDict takes O(1).
    
The space complexity of get method is O(n)
    - self.cache_dict can have the size of the number of element. 

**set method**
The time complexity of set method is O(1)
    - To check if a key exists in an OrderedDict takes O(1).
    - remove_least_recently_used uses popitem of OrderedDict which takes O(1)
    - get an element by key from an OrderedDict takes O(1).
    
    
The space complexity of set method is O(n)
    - self.cache_dict can have the size of the number of element. 



