import os
print(__file__)
print(type(__file__))

print(os.path.realpath(__file__))
print(type(os.path.realpath(__file__)))

print(os.path.dirname(os.path.realpath(__file__)))
print(type(os.path.dirname(os.path.realpath(__file__))))

print(os.path.dirname(__file__))