#this is file 1

def funcion1(x,y):
    print(f"x = {x}, y = {y}")

print(f"this is a print statement in file 1. name = {__name__}")


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




if __name__ == "__main__":
    main()    