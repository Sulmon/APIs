#this will help us understand type annotations
from collections import namedtuple
from typing import Iterable, Optional

Item = namedtuple("Item", "name, value")

#this means it can be an integer but also a None which is not an integer
running_max: Optional[int]= None 


def counter(items: Iterable[Item]): 
# this was our program is much more structured and knows what to expect ,if we give in 7 then it will say no
# i am expecting something iterable
            
    global running_max
    total = 0

    for i in items:
        total += i.value

    if not running_max or total > running_max:
        running_max = total

    return total


def main():
    print("Let's create some items")

    dinner_items = [Item('Pizza', 20), Item('Beer', 9), Item('Beer', 9)]
    breakfast_items = [Item('Pancakes', 11), Item('Bacon', 4), Item('Coffee', 3), Item('Coffee', 3), Item('Scone', 2)]

    dinner_total = counter(dinner_items)

    print(f"Dinner was ${dinner_total:,.02f}")

    breakfast_total = counter(breakfast_items)
    print(f"Breakfast was ${breakfast_total:,.02f}")

    print(f"Today your most expensive meal costs ${running_max:.02f}")


#runs the main function if the name after def is main
if __name__ == '__main__':
    main()