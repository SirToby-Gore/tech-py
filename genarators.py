list: int = [
    1,2,3,44,5,5,6,67,7,8,8,88,8,6,6,65,5
]

from typing import Generator
import time

def genny() -> Generator:
    counter: int = 0

    while True:
        yield counter

        counter += 1

        if counter > 9:
            counter = 0

pheonix: Generator = genny()

print('\n\n')
#
for i in range(1000):
    print(next(pheonix), end='\r')
    time.sleep(0.3)