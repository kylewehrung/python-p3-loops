#!/usr/bin/env python3

def happy_new_year():
    for i in range(10, 0, -1):
        print(i)

    print("Happy New Year!")
happy_new_year()




def square_integers(int_list):
    square_these_bad_boys = [num * num for num in int_list]
    return (square_these_bad_boys)

square_integers([1, 2, 3, 4, 5])

# def square_integers(int_list):
    



def fizzbuzz():
    for i in range(1, 101, +1):
        if i % 3 == int() and i % 5 == int():
            print("FizzBuzz")
        elif i % 3 == int():
            print("Fizz")
        elif i % 5 == int():
            print("Buzz")
        else:
            print(i)
fizzbuzz()