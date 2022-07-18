# Greeting function
@classmethod
class Greet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greeting(self):
        print("Hello my name is {} and my age is {}".format(self.name, self.age))
# Taking input
g = Greet(str(input("Enter your name : ")), int(input("Enter your age : ")))
# Calls the function
g.greeting()