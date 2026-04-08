import random

def howmany():

    times = random.randint(1, 100)
    
    while times > 0:
        print(f"the {times} times")
        print("hello world")

        times -= 1 


howmany()