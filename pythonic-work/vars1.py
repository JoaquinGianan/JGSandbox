# file to work out the vars().items() function and to make it work...

if __name__ == "__main__":
    luna = "apolo"
    luna_nueva = "sand 02"
    futura_luna = "sand 03"
    futura = 'sand 04'

    lista_variables = list(vars().items())
    for item in lista_variables:
        print(item)

    print(f"ver si corre el val")

def ver_variables_locales2():  # var(), inside a function, is looking only at locals(), but within the function...
    print("running")
    montana = "flyfishing"
    lista = list(vars().items())
    for algo in lista:
        print(algo)   


   


def ver_variables_globales3():  
    print("running ver-variables-globales3")
    lista = list(globals().items())
    for algo in lista:
        print(algo)

if __name__ == "__main__":
    ver_variables_globales3()        
    ver_variables_locales2()     
    print(list(vars().items()))