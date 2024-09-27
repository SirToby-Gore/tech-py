def pickle_write(object: any, path: str = "data.pickle") -> None:
    '''
    > this allows one to save any object to a .pickle file
    '''
    if not path.endswith('.pickle'):
        raise ValueError('path must be a .pickle file')

    import pickle

    with open(path, 'wb') as f:
        pickle.dump(object, f)
    
    print(f'pickled {object} to {path}')

def pickle_read(path: str = "data.pickle") -> any:
    '''
    > this allows you to load any object from a .pickle file
    '''
    if not path.endswith('.pickle'):
        raise ValueError('path must be a .pickle file')

    import pickle

    with open(path, 'rb') as f:
        print(f'returned {object} to {path}')
        return pickle.load(f)


from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    height: float

    def __str__(self) -> str:
        return f"My name is {self.name}, I am {self.age}yrs old, I am also {self.height}."

    def to_map(self) -> dict:
        return {
            'name': self.name,
            'age': self.age,
            'height': self.height
        }

def pick_example() -> None:
    '''
    ## This example on how to use pickle

    I will show you how to use pickle to save and load objects

    The above functions will show you how to save and load objects

    The below code will only show how to use those functions

    ## What do you use pickle for?

    You use it store any object instance in a .pickle file so that
    the data is not lost between runtime sessions of the file, or it can be used in multiple files
    '''

    person = Person('John', 30, 180)

    pickle_write(person)

    pickle_read(person)


# -----
# below here is how to use json
# -----


def json_write(object: iter, path: str = "data.json") -> None:
    '''
    > this all allows one to save any object to a .json file
    '''

    if not path.endswith('.json'):
        raise ValueError('path must be a .json file')

    import json

    with open(path, 'w') as f:
        f.write(
            json.dump(
                object,
                f
            )
        )

def json_read(path: str = "data.json") -> iter:
    '''
    > takes in a .json path and returns a dict or list
    '''

    if not path.endswith('.json'):
        raise ValueError('path must be a .json file')

    import json

    with open(path, 'r') as f:
        return json.load(f)

def json_example() -> None:
    '''
    ## This is an example on JSON

    I will show you how to use json to save and load objects

    The above functions will show you how to save and load objects

    The below code will only show how to use those functions

    ## Why use JSON?

    * JSON is a format for storing and transporting data
    * It is a human readable format
    * It is a lightweight format
    * it is also widley used in day to day applications
    * it also allows you to store data that does not require any order
    '''

    players = {
        'john' : {
            'name': 'john',
            'play-time' : 10,
            'level': 30,
            'coins' : 472
        },
        'jane' : {
            'name': 'jane',
            'play-time' : 37,
            'level': 54,
            'coins' : 999
        },
        'bob' : {
            'name': 'bob',
            'play-time' : 56,
            'level': 80,
            'coins' : 2100
        },
        'alice' : {
            'name': 'alice',
            'play-time' : 19,
            'level': 23,
            'coins' : 450
        },
    }

    json_write(players)

def main() -> None:
    pick_example()

    json_example()

if __name__ == "__main__":
    main()