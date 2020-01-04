# In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
child_2 = Group('child_2')
sub_subchild = Group('sub_subchild')
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
child.add_group(sub_subchild)

sub_subchild_user = 'sub_sub_child_user'
sub_subchild.add_user(sub_subchild_user)


# Write a function that provides an efficient look up of whether the user is in a group.
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.users:
        return True
    else:
        for sub_group in group.groups:
            if is_user_in_group(user, sub_group):
                return True
        return False


# Tests:
# This one should return True
result = is_user_in_group(sub_child_user, parent)
print("result: {}".format(result))

# This one should return False
result = is_user_in_group('random', parent)
print("result: {}".format(result))

# This test tests more than two layers, This one should return True
result = is_user_in_group('sub_sub_child_user', parent)
print("result: {}".format(result))

# This test tests more than two layers, This one should return True
result = is_user_in_group('sub_sub_child_user', child)
print("result: {}".format(result))

# This test tests more than two layers, This one should return False
result = is_user_in_group('sub_sub_child_user', child_2)
print("result: {}".format(result))
