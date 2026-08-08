from greeting import greet, goodbye, good_morning
from helper import print_line

name = input("Enter your name: ")

print_line()
greet(name)

print_line()
goodbye(name)

print_line()
good_morning(name)
