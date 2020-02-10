# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, part=None, handler=None):
        # Initialize the node with children as before, plus a handler
        self.part = part
        self.handler = handler
        self.children = {}

    def insert(self, part, handler=None):
        # Insert the node as before
        if self.part == part:
            return self  # TODO: Can you return self like this?
        if part in self.children:
            return
        new_node = RouteTrieNode(part, handler)
        self.children.update({part: new_node})
        return new_node


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode('/')

    def insert(self, parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for part in parts:
            if node.part == part:
                continue
            if part in node.children:
                node = node.children[part]
            else:
                new_node = node.insert(part)
                node = new_node
        node.handler = handler

    def find(self, parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for part in parts:
            if node.part == part:
                continue
            if part in node.children:
                node = node.children[part]
            else:
                return None

        return node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, route_handler):
        self.route_trie = RouteTrie()
        self.route_trie.root.handler = route_handler

    # Create a new RouteTrie for holding our routes
    # You could also add a handler for 404 page not found responses as well
    def add_handler(self, path, handler):
        parts = self.split_path(path)
        self.route_trie.insert(parts, handler)

    # Add a handler for a path
    # You will need to split the path and pass the pass parts
    # as a list to the RouteTri
    def lookup(self, path):
        parts = self.split_path(path)
        return self.route_trie.find(parts)

    # lookup path (by parts) and return the associated handler
    # you can return None if it's not found or
    # return the "not found" handler if you added one
    # bonus points if a path works with and without a trailing slash
    # e.g. /about and /about/ both return the /about handle
    def split_path(self, path):
        if path == "/":
            return ['/']
        if path.endswith('/'):
            path = path[:-1]
        return [element +'/' for element in path.split('/')]


# you need to split the path into parts for
# both the add_handler and loopup functions,
# so it should be placed in a function her
# Here are some test cases and expected outputs you can use to test your implementatio
# create the router and add a route

router = Router("root handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a rout
# # some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
