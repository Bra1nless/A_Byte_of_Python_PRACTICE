class Robot():
    population = 0

    def __init__(self, name):
        self.name = name
        print(f'(Initiation of {self.name})')
        Robot.population += 1

    def __del__(self):
        print(f'{self.name} is in process if termination')
        Robot.population -= 1
        if Robot.population == 0:
            print(f'{self.name} was the last of greate Robot Nation!')
        else:
            print(f'There are {Robot.population} more Robots! We are '
                  f'going to defeat the Humanity!')

    def sayHi(self):
        print(f'Hello, pathetic humans! My name is {self.name}! BEWARE!!!')

    @staticmethod
    def howMany():
        print(f'There are {Robot.population} Proud Robots! We are '
              f'going to defeat the Humanity!')


droid1 = Robot('R2D2')
droid1.sayHi()
Robot.howMany()
droid2 = Robot('C3Po')
droid2.sayHi()
Robot.howMany()

print(10*'-')

print('Now Humanity is going to destroy all stupid robots!')
print(10*'-')

del droid1
del droid2

Robot.howMany()
