#a = "ncdbhbhbc"
 #while True:
    #if not a: 
       # break
    #a = a[:-1]

#print(a)


class User:

    def __init__(self, name, email, age):
     self.name = name
     self.email = email
     self.age = age

    def greeting(self):
      return f'My name is {self.name}. I am {self.age}'

    def has_birthday(self):
        self.age += 1

class Customer(User):
    def __init__(self, name, email, age):
      self.name = name
      self.email = email
      self.age = age
      self.balance = 0

    def set_balance(self, balance):
     self.balance = balance

     def greeting(self):
      return f'My name is {self.name}. I am {self.age} and my balance is {self.balance}'

brad = User('BradTraversy', 'marykidun@gmail.com', 35)
janet = Customer('Janet', 'mary@gmail.com', 28)

janet.set_balance(500)
print(janet.greeting())

brad.has_birthday()
print(brad.greeting())


