class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print('inhale, exhale')

# for class fish to have the features of class animal,
# use a parenthesis and add the class which you want to  add inside and the add an initializer


class Fish(Animal):
    def __init__(self):
        super().__init__()
    def swim(self):
        print('moving in water')
    "modifying an inherited function"
    def breathe(self):
        super().breathe()
        print('inside water')


nemo = Fish()
nemo.swim()
print(nemo.num_eyes)
nemo.breathe()