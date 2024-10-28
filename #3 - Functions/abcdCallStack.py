#this code was made to understand the frame object of the call stack
#I made this line to understand the code better
from PIL import Image
img = Image.open(r"#3 - Functions\abcdCallStack.png")


def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()
img.show()