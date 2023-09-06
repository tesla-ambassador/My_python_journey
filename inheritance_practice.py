
# Online Python - IDE, Editor, Compiler, Interpreter

class Human:
    def __init__(self):
        self.name = ''
        self.gender = 0
        
    def how_many_genders(self):
        self.gender = 2
        print(f'Hello, I am {self.name} and there are only {self.gender} genders')
    
class Fools(Human):
    def __init__(self):
        super().__init__()
    
    def how_many_genders(self):
        # super().how_many_genders()
        self.gender = 6
        print(f'Hello I am {self.name}, there are {self.gender} plus genders')
        
fool = Fools()
fool.name = 'Karen'
fool.how_many_genders()


