def function_types(arg: int) -> int:
    '''
    > This function says that the one arg is an int, but python
    is not strict so you can pass in a str
    '''

def function_args(*args) -> None:
    '''
    > The * before an arg allows you to pass in an as list of
    unknown length or content
    
    would use it like so
    ```
    # python

    pizza_toppings("pepperoni", "chicken", "pepper")
    ```
    or
    ```
    # python

    options: list = ["pepperoni", "chicken", "pepper"]
    pizza_toppings(*options)
    ```
    '''
    for arg in args:
        print(arg)

def function_kwargs(**kwargs) -> None:
    '''
    > The double ** allows you to pass in kwargs(key word arguments)
    
    this means you use it like so
    ```
    # python 

    pizza(
        base="thin",
        sauce="tomato",
        toppings=[
            "pepperoni",
            "chicken",
            "pepper"
        ],
        time=DateTime(17,8,2024))
    ```
    or
    ```
    # python
    
    map: dict = {
        "base": "thin",
        "sauce": "tomato",
        "toppings": [
            "pepperoni",
            "chicken",
            "pepper"
        ],
        "time": DateTime(17,8,2024)
    }

    pizza(**map)
    ```
    '''
    for key, value in kwargs:
        print(key, value)

def function_positional(arg1, arg2, /, kwargs) -> None:
    '''
    > using a slash makes anything that comes before it have to be passed positionally

    this will cause an error
    ```
    # python 

    function_positional(arg2=2, arg1=6, **kwargs)
    ```
    you will have to use it like so
    ```
    # python

    function_positional(6, 2, **kwargs)
    ```
    '''

def function_recursion(i: int) -> int:
    '''
    > this function returns the sum of every number of itself and
    every number below itself
    '''
    if i > 1:
        return function_recursion(i-1) + i
    else: 
        return i