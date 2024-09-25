class Person:
    def __init__(self, name: str, age: int, height: float) -> None:
        self.name: str = name
        self.age: int = age
        self.height: float = height

    def grow(self, amount_by: float) -> None:
        self.height += amount_by

    def birthday(self) -> None:
        self.age += 1
    
    def describe_me(self) -> str:
        return f"My name is {self.name}, I am {self.age}yrs old, I am also {self.height}."
    
bob: Person = Person('Bob', 15, 1.0)
print(bob.describe_me())

bob.grow(2.30)
print(bob.describe_me())

bob.birthday()
print(bob.describe_me())


class Alien(Person):
    def birthday(self) -> None:
        self.age += 1
        self.height += 0.3

ridley: Alien = Alien('ridley', 103, 4.05)

print(ridley.describe_me())

ridley.birthday()

print(ridley.describe_me())

print(ridley.age)

class Statics:
    @staticmethod
    def method1(arg: str) -> str:
        '''
        use static methods when you do not need to self with in this function
        '''

        return arg*3
    
    def method2(self, arg: str) -> str:
        '''
        to use self you must call this method from a pre existing object
        '''
        return f'this is a {self.method1(arg)} nested'


class Duck:
    def __init__(self) -> None:
        pass

    def quack(self) -> None:
        print('Quack!!!')
    
class RubberDuck(Duck):
    def quack(self) -> None:
        print('squeak')

mallard: Duck = Duck()
toy_duck: RubberDuck = RubberDuck()

my_ducks: list[Duck | RubberDuck] = [mallard, toy_duck]

for duck in my_ducks:
    duck.quack()

class ComplexClass:
    def __init__(self) -> None:
        pass

    def __str__(self):
        '''
        # making a __ method

        This means to use one of pythons type conversions.

        You could have `__int__` to use
        ```
        int(class_object)
        ```.

        In this case `__str__` is used.

        Meaning if you want a string of your class you can define how to do that with the func
        ```
        str(class_object)
        ```
        '''
        pt1: str = str(self.non_str_val)
        pt2: str = str(self.number_of_things)

        return pt1 + pt2
    
