# the task condition is placed in the README file
# https://github.com/codeschool43/Build_in_function_homework#build_func10
from tkinter import Y


def main(x,y):
    answer=3*pow(y,1/2)+pow(x,2/3)
    return round(answer,2)
print(main(8,4))
