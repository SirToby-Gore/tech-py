'''
* str
    - used for words
    - str is short for string
    - you can get f-string
    - which is where you put an f before a string in python allowing you to use squiggly brackets to inline variables
    - you can use format on a normal string in args passed in for each position per each bracket pair
    - or formatmap where you pass in a dict to allow you format over pre-defined bits in a string. 
    ```
    name: str = 'bob'
    age: int = 36
    height: float = 1.6 # in m(s)
    f_string: str = f'my name is {name} and I am {age} years old, I am also {height} meters tall'

    format_string: str = 'my name is {} and I am {} years old, I am also {} meters tall'.format(
        name,
        age,
        height
    )

    map_string: str =  'my name is {name} and I am {age} years old, I am also {hight} meters tall'.formatmap(
        {
            'name': name,
            'age': age,
            'height': height
        }
    )
    ```
* chr
    - used for single characters
    - chr is short for character
* int
    - used for whole numbers
    - negatives are are int(s) too in python as they are signed
    - int is short for integer
* float
    - floats are used for real numbers
    - real numbers or decimal numbers
    - floats are less accurate than int(s) but have more range or expressions
    - float is short for floating point number
* doubles
    - double uses double the bits of a float
    - this means they have more accuracy
    - otherwise the same type
* bool
    - this came the mathematic Bool
    - he came up with the idea that all maths could be put into 'yes' and 'no' question
    - bool are very small at one bit in size '1' or '0'
    - as they are binary they can be used with int(s) of '1' and '0'
    - because python is weird you use it add 'True' or 'False' using capitals
* list(array)
    - this is serries of joined values by index from 0
    - in python you can call the function enumerate() to make a dict of a list 
    - with the keys = the index
    - you can pass in the arg of start = x, to change what it starts from
* dict(map)
    - these are key value pairs
    - like in a list you have index's to reference where an item is, in a dict you have keys
    - may have a key of hair colour,
    ```python
    person['hair colour'] = 'brown'
    ``` 
    - use dicts when there is not given structure to a data set
    - they are also known as json(s)
    - you can import JSON to cast into a json safe format
    - or import from a .json into a dict or list
* set
    - this is list but with unique values
* None(null)
    - this represents nothing
* generators
    - to use this you must 
    ```python
    from typing import Generator
    ```
    - these are functions that halt and resume what they return in the run time of a program
    - they save memory and complexly in a code base
    - rather than building into the main() or pre-generated values
* lambda
    - these are anonyms functions
    - there is no need for return statements
    - they can only be 1 to 3 lines long
    - they are used mainly in args for functions
* any
    - this is reference and default in python for a variable that can be anything
    - this should be used in type annotation for function returns, as the default is None
'''

def eggs(spam) -> list | str | bool | None: 
    '''
    # big header

    ## header

    ###### tiny header < use a hashtag for a heading, 1 for the biggest header;
    # use 6 for the smallest>

    * bullet point
    * second bullet point
        - nested bullet point

    1. number bullet point

    **this is in bold**

    *this is in italic*

    ***this is very important***

    this is on a newline
    this is not :(

    ```
    print("hello world")
    ```

    `return`

    > this is a back quote

    [this is a link](https://google.com)
    '''
    
    return f"this is a string {spam}"



listy: list[int | float] = [
    1,
    2.4,
    4,
    46,
    3.9,
    4.2
]

print()

for var in listy:
    print(var)
if listy[1] == 2.4:
    print('listy at pos 1 was 2.4')
else:
    print('it was not')


match input('y/n'):
    case "y":
        print('you typed y')
    case "n":
        print('you typed n')

    case other:
        print('I dunno what you typed')

inp: str = input()

if inp == "y":
    do_a_thing()
elif inp == "n":
    do_a_diffrent_thing()
else:
    dunno()

