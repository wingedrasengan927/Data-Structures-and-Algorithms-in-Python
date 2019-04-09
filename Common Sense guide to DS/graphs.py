
# let's create a graph data structure
# it shows relationships of people

# this is an example of a directed graph. based off twitter

class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, name):
        '''adds a friend to the person'''

        self.friends.append(name)

    def show_friends(self):
        '''prints all the friends'''

        print(self.friends)


john = Person("john")
john.add_friend("katy")
john.add_friend("halsey")
john.add_friend("poker")

john.show_friends()
print(john.name)