# file 3 is simmilar to file1 but with no name = main

#this is file 1

def funcion1(x = 0,y = 0):
    print(f"x = {x}, y = {y}")

print(f"this is a print statement in file 3. name = {__name__}")


def main():

    i = 33
    x = "pedro"    
    i = i *2
    print(i)
    # print(locals().items())

    # print(globals().items())

    # print(vars().items())

    for n in range(3):
        print(i)

luna = "apolo"

print(f"listing by hand 1 ...")
lista_variables = list(vars().items())
for item in lista_variables:
    print(item)




def ver_variables_locales():  # this function is not working or ...
    lista_variables = list(vars().items())
    for item in lista_variables:
        print(item)
       
print("ver variables")
x = 657
apolo = "luna"
ver_variables_locales()  # ... this function call is not working
print("se vieron?")     

print(f"listing by hand 2 ...")
lista_variables = list(vars().items())
for item in lista_variables:
    print(item)