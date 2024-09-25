# str, int, float, doubles, bool, list(arrays), dict(maps), set, None(null), generators, lambda

def eggs(spam) -> list | str | bool | None:
    '''
    # big header

    ## header

    ###### tiny header < use a hastag for a heading, 1 for the biggest header; use 6 for the smallest>

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

