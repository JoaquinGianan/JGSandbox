#this is file 2

print(f"this is a print statement in file 2. name = {__name__}")


import file1

for i in range(3):
    print(i)

# print(locals().items())
# print(globals().items())
# print(vars().items())

print(vars().items())


file1.funcion1(2,8)