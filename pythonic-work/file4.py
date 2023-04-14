#this is file4.  simmilar to file2

print(f"this is a print statement in file 4. name = {__name__}")
print(f"this is always printed in file4.")

import file3

for i in range(3):
    print(i)

# print(locals().items())
# print(globals().items())
# print(vars().items())

from file3 import funcion1

funcion1(2,8) #importing the function

file3.funcion1(8) #calling as a method

lista_variables = list(vars().items())
for item in lista_variables:
    print(item)

print(f"ver si corre el val")

def ver_variables_locales2():  # this function is not working or ...
    print("uno")
    lista = list(vars().items())
    for algo in lista:
        print(algo)


ver_variables_locales2()        
