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
    
    if user is None or group is None:
        print("Empty input")
        return
    
    elif type(user) != str:
        print("Invalid input")
        return
    
    users = group.get_users()
    groups = group.get_groups()
    
    if user in users:
        print('True: User is found in the group!')
        return
    else:
        for group in groups:
            is_user_in_group(user,group)
            return
    print("False: User is not in the group")
    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print("\n")
print("Test 1")
is_user_in_group(sub_child_user, parent)

print("\n")
print("Test 2")
user = "This is test 2"
child.add_user(user)
is_user_in_group(user, parent)

print("\n")
print("Test 3")
user = "Hello world!"
is_user_in_group(user, parent)

print("\n")
print("Edge test 1: empty input")
user = None
is_user_in_group(user, parent)

print("\n")
print("Edge test 2: invalid input")
user = 123456
is_user_in_group(user, parent)