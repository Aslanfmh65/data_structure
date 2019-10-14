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

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group in parent.get_groups():
        if user in parent.get_users():
            return True
        else:
            return False
    elif group in child.get_groups():
        if user in child.get_users():
            return True
        else: False
    else:
        if user in sub_child.get_users():
            return True
        else:
            return False

parent = Group("parent")
child = Group("child")
sub_child = Group('subchild')

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)


print('Normal Cases:')
## Test 1
print(is_user_in_group(user='parent_user', group=parent))
# False

## Test 2
print(is_user_in_group(user='child_user', group=parent))
# False

## Test 3
print(is_user_in_group(user='sub_child_user', group=parent), '\n')
# True

# Edge Cases:
print('Edge Cases:')
## Test 4
print(is_user_in_group(user='', group=parent))
# False

## Test 5
print(is_user_in_group(user='', group=child))
# False