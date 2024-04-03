class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print('respirou')


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def swim(self):
        print("nadando")


nemo = Fish()
nemo.breathe()
nemo.swim()