import subprocess
import os
import random

##print a beatiful line
def whiteline():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

##clear terminal
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

"""
                     odd or not test
 if number is odd return True else False
 
"""
def is_odd(number):
    if number%2 == 1:
        return True
    else:
        return False


##run a Python file 
def run(file):
    subprocess.run(["python", file])
    
    
##random number
def randomize(num1,num2):
    return random.randint(num1,num2)
    
##printing colored
def hex_to_256(hex_color):
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return 16 + (36 * (r // 51)) + (6 * (g // 51)) + (b // 51)

def hex_text(hex_color, text):
    color_code = hex_to_256(hex_color)
    return f"\033[38;5;{color_code}m{text}\033[0m"

def colorize(color,text):
    print(hex_text(color, text))
