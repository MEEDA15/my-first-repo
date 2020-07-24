class Pypet:
    def __init__(self,name,age,weight,photo):
        self.hungry = True
        self.bored = True
        self.name = name
        self.age = age
        self.weight = weight
        self.photo = photo

    def speak(self):
        print('hello my name is' + ' '+ self.name + ' and i look like this:' + self.photo )
        if self.hungry:
            print('and im hungry')

        if self.bored:
            print('and im bored')

        if not self.hungry and not self.bored:
            print('and im happy')



    def feed(self):
        self.hungry = False
        self.weight += 0.1

    def play(self):
        self.bored = False


